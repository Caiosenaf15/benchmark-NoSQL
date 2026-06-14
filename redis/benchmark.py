import os, time, json, hashlib, hmac, threading, datetime, pathlib
import psutil, bcrypt
from argon2 import PasswordHasher
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from config import*

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
    avg = lambda l: round(sum(l)/max(len(l),1), 2)
    return {
    "test": name,
    "iterations": iters,
    "total_s": round(elapsed, 4),
    "ops_per_sec": round(iters/elapsed, 2),
    "avg_ms": round(elapsed/iters*1000, 4),
    "avg_cpu_pct": avg(cpu_s),
    "avg_ram_pct": avg(ram_s),
    "peak_cpu": max(cpu_s, default=0),
    "peak_ram": max(ram_s, default=0),
    }

def crypto_tests(size, iters):
    payload = os.urandom(size)
    key32 = os.urandom(32)
    iv = os.urandom(16)
    password = b"senha_benchmark_2026"
    ph = PasswordHasher(time_cost=1, memory_cost=65536, parallelism=2)
    ct = aes_encrypt(payload, key32, iv)
    tests = [
    ("sha256", lambda: hashlib.sha256(payload).digest()),
    ("sha512", lambda: hashlib.sha512(payload).digest()),
    ("hmac_sha256", lambda: hmac.new(key32, payload, hashlib.sha256).digest()),
    ("aes256_enc", lambda: aes_encrypt(payload, key32, iv)),
    ("aes256_dec", lambda: aes_decrypt(ct, key32, iv)),
    ("bcrypt_hash", lambda: bcrypt.hashpw(password, bcrypt.gensalt(rounds=10))),
    ("argon2_hash", lambda: ph.hash(password.decode()))
    ]
    return [run_test(name, fn, iters) for name, fn in tests]

def benchmark_redis(size, iters):
    import redis as redis_lib
    r = redis_lib.Redis(host=REDIS_HOST, port=REDIS_PORT)
    r.flushdb()

    password = b"senha_benchmark_2026"
    ph = PasswordHasher(time_cost=1, memory_cost=65536, parallelism=2)
    payload = os.urandom(size)
    key32 = os.urandom(32)
    iv = os.urandom(16)
    ct = aes_encrypt(payload, key32, iv)
    counter = [0]

    results = []

    results.append(run_test(
        "insert_aes256",
        lambda: r.set(f"aes:{counter[0]}", 
            aes_encrypt(payload, key32, iv)
            ) or counter.__setitem__(0, counter[0]+1),
        iters
    ))

    results.append(run_test(
        "insert_sha256",
        lambda: r.hset(f"sha:{counter[0]}", mapping={
            "data": payload.hex(),
            "hash": hashlib.sha256(payload).hexdigest()
        }) or counter.__setitem__(0, counter[0]+1),
        iters
    ))

    results.append(run_test(
        "insert_hmac_sha256",
        lambda: r.hset(f"hmac:{counter[0]}", mapping={
            "data":payload.hex(),
            "hmac": hmac.new(key32, payload, hashlib.sha256).hexdigest()
        }) or counter.__setitem__(0, counter[0]+1),
        iters
    ))

    results.append(run_test(
        "inset_bcrypt",
        lambda: r.set(
            f"bcrypt:{counter[0]}",
            bcrypt.hashpw(password, bcrypt.gensalt(rounds=10))
        ) or counter.__setitem__(0, counter[0]+1),
        iters
    ))

    results.append(run_test(
        "insert_argon2",
        lambda: r.set(
            f"argon2:{counter[0]}",
            ph.hash(password.decode())
        ) or counter.__setitem__(0, counter[0]+1),
        iters
    ))

    r.set("fixed:aes", ct)
    results.append(run_test(
        "read_decrypt_aes256",
        lambda: aes_decrypt(r.get("fixed:aes"), key32, iv),
        iters
    ))

    r.hset("fixed:sha", mapping={
        "data": payload.hex(),
        "hash": hashlib.sha256(payload).hexdigest()
    })
    results.append(run_test(
        "read_verify_sha256",
        lambda: (
            lambda d: hashlib.sha256(bytes.fromhex(d[b"data"].decode())).hexdigest() == d[b"hash"].decode()
        )(r.hgetall("fixed:sha")),
        iters
    ))

    results.append(run_test(
        "update_reencrypt_aes256",
        lambda: r.set("fixed:aes", aes_encrypt(payload, key32, iv)),
        iters
    ))

    r.set("del:key", ct)
    results.append(run_test(
        "delete_encrypted_record",
        lambda: r.delete("del:key") or r.set("del:key", ct),
        iters
    ))

    r.flushdb()
    return results

def main():
    out_dir = pathlib.Path("results")
    out_dir.mkdir(exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    print("\n== BENCHMARK CRIPTOGRAFIA INTEGRADA - REDIS ==\n")
    all_results = {"timestamp": ts, "db": "redis", "results": {}}
    for size in DATA_SIZES:
        print(f"--- payload={size}B ---")
        key = f"size_{size}"
        all_results["results"][key] = benchmark_redis(size, ITERATIONS)
        for r in all_results["results"][key]:
            print(f" {r['test']:30s} {r['ops_per_sec']:>10.1f} ops/s | {r['avg_ms']:.4f} ms | CPU {r['avg_cpu_pct']}%")
    out_file = out_dir / f"crypto_benchmark_redis_{ts}.json"
    with open(out_file, "w") as f:
        json.dump(all_results, f, indent=2)
        print(f"\nResultado salvo em: {out_file}")

if __name__ == "__main__":
    main()
