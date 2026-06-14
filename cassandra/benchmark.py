import os, time, json, hashlib
import hmac, threading, datetime, pathlib
import psutil, bcrypt
from argon2 import PasswordHasher
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from config import *

def aes_encrypt(data, key, iv):
    c = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    e = c.encryptor()
    return e.update(data) + e.finalize()

def aes_decrypt(ct, key, iv):
    c = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    d = c.decryptor()
    return d.update(ct) + d.finalize()

def monitor(stop, cpu_s, ram_s):
    while not stop.is_set():
        cpu_s.append(psutil.cpu_percent(interval=0.05))
        ram_s.append(psutil.virtual_memory().percent)

def run_test(name, fn, iters):
    cpu_s, ram_s = [], []
    stop = threading.Event()
    t = threading.Thread(target=monitor, args=(stop, cpu_s, ram_s), daemon=True)
    t.start()
    start = time.perf_counter()
    for _ in range(iters):
        fn()
    elapsed = time.perf_counter() - start
    stop.set(); t.join()
    avg = lambda l: round(sum(l)/max(len(l), 1), 2)
    return {
        "test": name,
	"iterations": iters,
	"total_s": round(elapsed, 4),
	"ops_per_sec": round(iters/elapsed, 2),
	"avg_ms": round((elapsed/iters)*1000, 4),
	"avg_cpu_pct": avg(cpu_s),
	"avg_ram_pct": avg(ram_s),
	"peak_cpu": max(cpu_s, default=0),
	"peak_ram": max(ram_s, default=0),
    }

def benchmark_cassandra(size, iters):
    from cassandra.cluster import Cluster
    from cassandra.policies import DCAwareRoundRobinPolicy
    import uuid
    cluster = Cluster(
        CASSANDRA_HOSTS,
        load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1')
    )
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS benchmark
        WITH replication = {'class':'SimpleStrategy','replication_factor':'1'}
    """)
    session.set_keyspace("benchmark")
    session.execute("DROP TABLE IF EXISTS crypto_ops")
    session.execute("""
        CREATE TABLE crypto_ops (
            id UUID PRIMARY KEY,
            data TEXT,
            hash_value TEXT,
            iv TEXT
        )
    """)
    key32 = os.urandom(32)
    iv = os.urandom(16)
    password = b"senha_benchmark_2026"
    ph = PasswordHasher(time_cost=1, memory_cost=65536, parallelism=2)
    payload = os.urandom(size)
    ct = aes_encrypt(payload, key32, iv)


    ins_aes = session.prepare("INSERT INTO crypto_ops (id, data, iv) VALUES (?, ?, ?)")
    ins_sha = session.prepare("INSERT INTO crypto_ops (id, data, hash_value) VALUES (?, ?, ?)")
    ins_hmac = session.prepare("INSERT INTO crypto_ops (id, data, hash_value) VALUES (?, ?, ?)")
    ins_pass = session.prepare("INSERT INTO crypto_ops (id, data) VALUES (?, ?)")
    upd = session.prepare("UPDATE crypto_ops SET data=?, iv=? WHERE id=?")
    dlt = session.prepare("DELETE FROM crypto_ops WHERE id=?")

    results = []

    results.append(run_test(
        "insert_aes256",
        lambda: session.execute(ins_aes,
            (uuid.uuid4(),
            aes_encrypt(payload, key32, iv).hex(),
	    iv.hex()
	)),
	iters
    ))

    results.append(run_test(
        "insert_sha256",
        lambda: session.execute(ins_sha,
            (uuid.uuid4(),
            payload.hex(),
            hashlib.sha256(payload).hexdigest()
        )),
        iters
    ))

    results.append(run_test(
        "insert_hmac_sha256",
        lambda: session.execute(ins_hmac,
            (uuid.uuid4(),
            payload.hex(),
            hmac.new(key32, payload, hashlib.sha256).hexdigest()
        )),
        iters
    ))

    results.append(run_test(
        "insert_bcrypt",
        lambda: session.execute(ins_pass,
            (uuid.uuid4(),
            bcrypt.hashpw(password, bcrypt.gensalt(rounds=10)).decode()
        )),
        iters
    ))

    results.append(run_test(
        "insert_argon2",
        lambda: session.execute(ins_pass,
            (uuid.uuid4(),
            ph.hash(password.decode())
        )),
        iters
    ))

    fixed_id = uuid.uuid4()
    session.execute(ins_aes, (fixed_id, ct.hex(), iv.hex()))
    sel = session.prepare("SELECT data, iv FROM crypto_ops WHERE id=?")
    results.append(run_test(
        "read_decrypt_aes256",
        lambda: aes_decrypt(bytes.fromhex(session.execute(sel, (fixed_id,)).one().data), key32, iv),
        iters
    ))

    fixed_id2 = uuid.uuid4()
    session.execute(ins_sha, (fixed_id2, payload.hex(), hashlib.sha256(payload).hexdigest()))
    sel2 = session.prepare("SELECT data, hash_value FROM crypto_ops WHERE id=?")
    results.append(run_test(
        "read_verify_sha256",
        lambda: (
            lambda row: hashlib.sha256(bytes.fromhex(row.data)).hexdigest() == row.hash_value)(session.execute(sel2, (fixed_id2,)).one()),
        iters
    ))

    results.append(run_test(
        "update_reencrypt_aes256",
        lambda: session.execute(upd, (aes_encrypt(payload, key32, iv).hex(), iv.hex(), fixed_id)),
        iters
    ))

    results.append(run_test(
        "delete_encrypted_record",
        lambda: session.execute(dlt, (fixed_id,)),
        iters
    ))

    session.execute("DROP TABLE IF EXISTS crypto_ops")
    cluster.shutdown()
    return results

def main():
    out_dir = pathlib.Path("results")
    out_dir.mkdir(exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    print("\n== BENCHMARK CRIPTOGRAFIA INTEGRADA - CASSANDRA ==\n")
    all_results = {"timestamp": ts, "db": "cassandra", "results": {}}
    for size in DATA_SIZES:
        print(f"--- payload={size}B ---")
        key = f"size_{size}"
        all_results["results"][key] = benchmark_cassandra(size, ITERATIONS)
        for r in all_results["results"][key]:
            print(f" {r['test']:30s} {r['ops_per_sec']:>10.1f} ops/s | {r['avg_ms']:.4f} ms | CPU {r['avg_cpu_pct']}%")
    out_file = out_dir / f"crypto_benchmark_cassandra_{ts}.json"
    with open(out_file, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResultado salvo em: {out_file}")

if __name__ == "__main__":
    main()
