# Reproducibility Package

## Overview

This repository contains the complete artifact package used in the experimental evaluation of cryptographic operations on NoSQL databases.

The benchmark compares:

* MongoDB 7.0
* Redis 7.x
* Apache Cassandra 5.x

The experiments evaluate the impact of cryptographic mechanisms on database performance.

Algorithms evaluated:

* AES-256
* SHA-256
* HMAC-SHA256
* bcrypt
* Argon2

Operations evaluated:

1. insert_aes256
2. insert_sha256
3. insert_hmac_sha256
4. insert_bcrypt
5. insert_argon2
6. read_decrypt_aes256
7. read_verify_sha256
8. update_reencrypt_aes256
9. delete_encrypted_record

---

## Experimental Environment

Hardware:

* CPU: Intel Core i5-12400F
* RAM: 32 GB
* GPU: NVIDIA RTX 4060

Operating System:

* Debian GNU/Linux 12 (Bookworm)
* Linux Kernel 6.1

---

## Dataset

The experiments use:

### RT-IoT2022

Source:

https://archive.ics.uci.edu/dataset/942/rt-iot2022

Records imported:

100,000

### YCSB

Version:

0.17.0

Workloads:

* A (50% Read / 50% Update)
* B (95% Read / 5% Update)
* C (100% Read)
* D (Read Latest)

---

## Repository Structure

benchmark/

├── config.py

├── import_dataset.py

├── benchmark_crypto.py

├── run_all.sh

├── collect_system_info.sh

├── results/

├── data/

└── docker/

---

## Installation

### Linux

Install dependencies:

```bash
./install_deps.sh
```

Run benchmark:

```bash
./run_all.sh
```

### Windows

Recommended:

* Docker Desktop
* WSL2 Ubuntu

Run:

```powershell
docker compose up
```

---

## Expected Outputs

results/

├── system_info.txt

├── ycsb_workload_a.txt

├── ycsb_workload_b.txt

├── ycsb_workload_c.txt

├── ycsb_workload_d.txt

└── crypto_benchmark.json

---

## Reproducibility Checklist

* [ ] Dataset downloaded
* [ ] Database installed
* [ ] Dependencies installed
* [ ] YCSB configured
* [ ] Benchmark executed
* [ ] Results generated

---

## Citation

Citation information for the article.
