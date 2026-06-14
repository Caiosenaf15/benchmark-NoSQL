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
    avg = lambda l: round(sum(l)/max(len(l),1), 2)
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

def benchmark_mongo(size, iters):
    from pymongo import MongoClient
    client = MongoClient(MONGO_URI)
    col = client["benchmark"]["crypto_ops"]
    col.drop()

    key32 = os.urandom(32)
    iv = os.urandom(16)
    password = b"senha_benchmark_2026"
    ph = PasswordHasher(time_cost=1, memory_cost=65536, parallelism=2)
    payload = os.urandom(size)
    ct = aes_encrypt(payload, key32, iv)

    results = []

    results.append(run_test(
        "insert_aes256",
        lambda: col.insert_one({
            "data": aes_encrypt(payload, key32, iv).hex(),
            "iv": iv.hex()
        }),
        iters
    ))

    results.append(run_test(
        "insert_sha256",
        lambda: col.insert_one({
            "data": payload.hex(),
            "hmac": hmac.new(key32, payload, hashlib.sha256).hexdigest()
        }),
        iters
    ))

    results.append(run_test(
        "insert_bcrypt",
        lambda: col.insert_one({
            "password_hash": bcrypt.hashpw(password, bcrypt.gensalt(rounds=10)).decode()
        }),
        iters
    ))

    results.append(run_test(
        "insert_argon2",
        lambda: col.insert_one({
            "password_hash": ph.hash(password.decode())
        }),
        iters
    ))

    doc_id = col.insert_one({
        "data": ct.hex(),
        "iv": iv.hex()
    }).inserted_id
    results.append(run_test(
        "read_decrypt_aes256",
        lambda: aes_decrypt(
            bytes.fromhex(col.find_one({"_id": doc_id})["data"]),
            key32, iv
        ),
        iters
    ))

    doc_id2 = col.insert_one({
        "data": payload.hex(),
        "hash": hashlib.sha256(payload).hexdigest()
    }).inserted_id
    results.append(run_test(
        "read_verify_sha256",
        lambda: (
            lambda d: hashlib.sha256(bytes.fromhex(d["data"])).hexdigest() == d["hash"]
        )(col.find_one({"_id": doc_id2})),
        iters
    ))

    results.append(run_test(
        "update_reencrypt_aes256",
        lambda: col.update_one(
            {"_id": doc_id},
            {"$set": {
                "data": aes_encrypt(payload, key32, iv).hex(),
                "iv": iv.hex()
            }}
        ),
        iters
    ))

    results.append(run_test(
        "delete_encrypted_record",
        lambda: col.delete_one({"_id": doc_id}),
        iters
    ))

    col.drop()
    client.close()
    return results

def main():
    out_dir = pathlib.Path("results")
    out_dir.mkdir(exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    print("\n== BENCHMARK CRIPTOGRAFIA INTEGRADA - MONGODB ==\n")
    all_results = {"timestamp": ts, "db": "mongodb", "results": {}}
    for size in DATA_SIZES:
        print(f"--- payload={size}B ---")
        key = f"size_{size}"
        all_results["results"][key] = benchmark_mongo(size, ITERATIONS)
        for r in all_results["results"][key]:
            print(f" {r['test']:30s} {r['ops_per_sec']:>10.1f} ops/s | {r['avg_ms']:.4f} ms | CPU {r['avg_cpu_pct']}%")
    out_file = out_dir / f"crypto_benchmark_mongo_{ts}.json"
    with open(out_file, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"Resultado salvo em: {out_file}")

if __name__ == "__main__":
    main()
