# Reproducibility Package

## Benchmarking the Impact of Cryptographic Mechanisms on NoSQL Databases

This repository contains the complete artifact package used to reproduce the experiments performed in the study evaluating the performance impact of cryptographic mechanisms on NoSQL database systems.

The benchmark evaluates the computational overhead introduced by encryption, hashing, and authentication mechanisms when integrated with common database operations.

---

## Abstract

Modern applications frequently store sensitive information in NoSQL databases, requiring cryptographic protections such as encryption, hashing, and message authentication.

This benchmark evaluates the performance impact of the following cryptographic mechanisms:

* AES-256
* SHA-256
* HMAC-SHA256
* bcrypt
* Argon2

The evaluation is performed on the following NoSQL database management systems:

* MongoDB
* Redis
* Apache Cassandra

The objective is to measure the effect of cryptographic operations on insertion, reading, updating, and deletion workloads.

---

## Experimental Environment

### Hardware

| Component | Specification        |
| --------- | -------------------- |
| CPU       | Intel Core i5-12400F |
| RAM       | 32 GB DDR4           |
| GPU       | NVIDIA RTX 4060      |
| Storage   | SSD                  |

### Operating System

| Component | Version                        |
| --------- | ------------------------------ |
| OS        | Debian GNU/Linux 12 (Bookworm) |
| Kernel    | Linux 6.x                      |

---

## Software Versions

The experiments were executed using the following software stack:

| Software  | Version |
| --------- | ------- |
| Python    | 3.x     |
| Java      | 21      |
| MongoDB   | 7.x     |
| Redis     | 7.x     |
| Cassandra | 5.x     |
| YCSB      | 0.17.0  |

---

## Benchmark Scope

The benchmark evaluates the following cryptographic operations.

### Encryption

* AES-256 Encryption
* AES-256 Decryption

### Hashing

* SHA-256
* bcrypt
* Argon2

### Authentication

* HMAC-SHA256

---

## Operations Evaluated

The following operations are benchmarked:

| Operation               | Description                     |
| ----------------------- | ------------------------------- |
| insert_aes256           | Encrypt and insert record       |
| insert_sha256           | Hash and insert record          |
| insert_hmac_sha256      | Generate HMAC and insert record |
| insert_bcrypt           | bcrypt hash insertion           |
| insert_argon2           | Argon2 hash insertion           |
| read_decrypt_aes256     | Read and decrypt                |
| read_verify_sha256      | Read and verify hash            |
| update_reencrypt_aes256 | Update and re-encrypt           |
| delete_encrypted_record | Delete encrypted record         |

---

## Workload Generation

The benchmark uses Yahoo! Cloud Serving Benchmark (YCSB) workloads.

### YCSB Version

0.17.0

### Workloads

#### Workload A

50% Reads

50% Updates

#### Workload B

95% Reads

5% Updates

#### Workload C

100% Reads

#### Workload D

Read Latest

---

## Experimental Data

No external datasets were used in the final experiments.

All benchmark records are generated and managed through YCSB workloads.

During the project design phase, external datasets were evaluated as potential data sources. However, due to compatibility issues across the evaluated database systems, the final benchmark relies exclusively on YCSB-generated workloads.

---

## Repository Structure

```text
benchmark/

├── README.md
│
├── scripts/
│   ├── benchmark_crypto.py
│   ├── run_all.sh
│   ├── collect_system_info.sh
│   └── validate_results.py
│
├── mongodb/
│   └── benchmark implementation
│
├── redis/
│   └── benchmark implementation
│
├── cassandra/
│   └── benchmark implementation
│
├── workloads/
│   ├── workload_a
│   ├── workload_b
│   ├── workload_c
│   └── workload_d
│
├── results/
│
└── docs/
```

---

## Installation

### Linux

Install dependencies:

```bash
sudo apt update

sudo apt install python3 python3-pip openjdk-21-jdk git
```

Clone repository:

```bash
git clone <repository-url>

cd benchmark
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

### Windows

Recommended options:

* Docker Desktop
* WSL2 Ubuntu

Install:

* Python 3.x
* Java 21
* Git

Clone repository:

```powershell
git clone <repository-url>

cd benchmark
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

## Running the Benchmark

### MongoDB

```bash
python mongodb/benchmark.py
```

### Redis

```bash
python redis/benchmark.py
```

### Cassandra

```bash
python cassandra/benchmark.py
```

---

## Running All Experiments

```bash
./scripts/run_all.sh
```

---

## System Information Collection

```bash
./scripts/collect_system_info.sh
```

The script collects:

* CPU information
* RAM information
* Operating system version
* Kernel version
* Storage information

---

## Output Files

Expected outputs:

```text
results/

├── mongodb_results.json
├── redis_results.json
├── cassandra_results.json
├── system_info.txt
└── benchmark_summary.csv
```

---

## Validation

To verify the execution:

```bash
python scripts/validate_results.py
```

Expected output:

```text
PASS

All benchmark executions completed successfully.
```

---

## Reproducibility Checklist

* [ ] Repository cloned
* [ ] Dependencies installed
* [ ] Java installed
* [ ] Python installed
* [ ] MongoDB configured
* [ ] Redis configured
* [ ] Cassandra configured
* [ ] YCSB configured
* [ ] Benchmark executed
* [ ] Results generated
* [ ] Results validated

---

## Limitations

Results may vary according to:

* Processor model
* Available memory
* Storage device
* Operating system
* Background processes

Relative performance trends should remain consistent.

---

## Citation

If you use this benchmark, please cite:

```bibtex
@misc{nosql_crypto_benchmark,
  title={Benchmarking the Impact of Cryptographic Mechanisms on NoSQL Databases},
  author={Author Names},
  year={2026}
}
```

---

## Contact

For questions regarding the benchmark implementation or reproduction process, please contact the authors.
