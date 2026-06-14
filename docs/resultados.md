---
title: "Resultados do Benchmark"
subtitle: "Benchmark do Impacto de Mecanismos Criptográficos em Bancos de Dados NoSQL"
author: "Caio Sena Freitas e Pedro Henrique T. Pinto — CEFET/RJ, Nova Friburgo"
date: "2026"
---

# 1. Arquivos de Resultados

Os resultados brutos completos (throughput, latência, uso de CPU e RAM por operação e tamanho de payload) estão disponíveis na pasta `results/` em formato JSON:

- `crypto_benchmark_redis_20260523_203720.json`
- `crypto_benchmark_mongo_20260523_114130.json`
- `crypto_benchmark_cassandra_20260523_135802.json`

Cada arquivo segue a estrutura:

```json
{
  "timestamp": "...",
  "system": { ... },
  "db": "redis | mongo | cassandra",
  "results": {
    "db_integration_size64":   [ { "test": "...", "ops_per_sec": ..., "avg_ms": ..., "avg_cpu_pct": ..., "avg_ram_pct": ..., "peak_cpu": ..., "peak_ram": ... }, ... ],
    "db_integration_size256":  [ ... ],
    "db_integration_size1024": [ ... ],
    "db_integration_size4096": [ ... ]
  }
}
```

# 2. Throughput Médio por Operação (ops/s)

Média aritmética entre os quatro tamanhos de payload (64, 256, 1.024 e 4.096 bytes).

| Operação | Redis | MongoDB | Cassandra |
|----------|------:|--------:|----------:|
| INSERT + AES-256 | 19.374 | 8.170 | 3.691 |
| INSERT + SHA-256 | 35.126 | 11.569 | 3.349 |
| INSERT + HMAC-SHA-256 | 32.805 | N/D | 3.204 |
| INSERT + Bcrypt | 20,3 | 20,2 | 19,5 |
| INSERT + Argon2 | 29,6 | 30,9 | 32,7 |
| READ + Decrypt AES-256 | 21.125 | 9.845 | 3.898 |
| READ + Verify SHA-256 | 31.468 | 11.494 | 4.636 |
| UPDATE + Re-encrypt AES-256 | 19.314 | 10.950 | * |
| DELETE registro criptografado | 27.882 | 15.133 | 3.678 |

\* Cassandra colapsa para 22,7 ops/s no payload de 4.096 bytes em INSERT, UPDATE e INSERT+HMAC, distorcendo a média; ver Seção 4.

# 3. Throughput Detalhado por Tamanho de Payload (ops/s)

## 3.1 INSERT + AES-256

| Banco | 64 B | 256 B | 1.024 B | 4.096 B |
|-------|-----:|------:|--------:|--------:|
| Redis | 19.913,9 | 20.150,5 | 19.313,3 | 18.118,7 |
| MongoDB | 9.256,1 | 6.624,9 | 8.760,0 | 8.039,6 |
| Cassandra | 4.239,5 | 5.603,0 | 4.898,1 | 22,7 |

## 3.2 INSERT + SHA-256

| Banco | 64 B | 256 B | 1.024 B | 4.096 B |
|-------|-----:|------:|--------:|--------:|
| Redis | 39.757,7 | 38.517,8 | 34.885,8 | 27.343,6 |
| MongoDB | 13.010,3 | 9.136,0 | 12.981,7 | 11.147,2 |
| Cassandra | 3.879,2 | 5.404,6 | 4.090,2 | 22,7 |

## 3.3 INSERT + HMAC-SHA-256

| Banco | 64 B | 256 B | 1.024 B | 4.096 B |
|-------|-----:|------:|--------:|--------:|
| Redis | 37.037,7 | 34.940,1 | 34.214,4 | 25.029,9 |
| MongoDB | N/D | N/D | N/D | N/D |
| Cassandra | 2.389,4 | 6.240,2 | 3.953,3 | 22,7 |

## 3.4 INSERT + Bcrypt / Argon2

| Métrica | Redis | MongoDB | Cassandra |
|---------|------:|--------:|----------:|
| Bcrypt — throughput médio (ops/s) | 20,3 | 20,2 | 19,5 |
| Bcrypt — latência média (ms/op) | 49,36 | 49,52 | 51,26 |
| Bcrypt — CPU média (%) | 8,32 | 8,33 | 8,50 |
| Argon2 — throughput médio (ops/s) | 29,6 | 30,9 | 32,7 |
| Argon2 — latência média (ms/op) | 33,82 | 32,32 | 30,62 |
| Argon2 — CPU média (%) | 15,26 | 15,17 | 15,66 |

## 3.5 READ + Decrypt AES-256

| Banco | 64 B | 256 B | 1.024 B | 4.096 B |
|-------|-----:|------:|--------:|--------:|
| Redis | 22.310,3 | 21.844,7 | 21.324,7 | 19.021,7 |
| MongoDB | 10.113,4 | 10.090,0 | 10.042,6 | 9.132,0 |
| Cassandra | 3.847,3 | 4.013,5 | 4.025,3 | 3.707,3 |

## 3.6 READ + Verify SHA-256

| Banco | 64 B | 256 B | 1.024 B | 4.096 B |
|-------|-----:|------:|--------:|--------:|
| Redis | 34.909,0 | 32.324,3 | 31.667,6 | 26.970,8 |
| MongoDB | 11.614,7 | 11.830,3 | 11.714,9 | 10.815,7 |
| Cassandra | 5.403,4 | 4.611,9 | 4.321,7 | 4.205,5 |

## 3.7 UPDATE + Re-encrypt AES-256

| Banco | 64 B | 256 B | 1.024 B | 4.096 B |
|-------|-----:|------:|--------:|--------:|
| Redis | 20.607,0 | 19.567,3 | 19.340,1 | 17.739,4 |
| MongoDB | 11.348,2 | 11.301,0 | 11.221,8 | 9.927,1 |
| Cassandra | 3.895,6 | 3.362,4 | 2.672,5 | 22,7 |

## 3.8 DELETE registro criptografado

| Banco | 64 B | 256 B | 1.024 B | 4.096 B |
|-------|-----:|------:|--------:|--------:|
| Redis | 29.025,1 | 27.801,4 | 27.018,0 | 27.684,0 |
| MongoDB | 14.637,8 | 14.803,1 | 15.155,7 | 15.134,4 |
| Cassandra | 3.913,2 | 3.029,1 | 2.994,5 | 4.773,0 |

# 4. Consumo de Recursos (CPU e RAM)

| Métrica | Redis | MongoDB | Cassandra |
|---------|------:|--------:|----------:|
| CPU média (operações leves) | 8,5% | 8,6% | 9,8% |
| CPU média (Bcrypt) | 8,32% | 8,33% | 8,50% |
| CPU média (Argon2) | 15,26% | 15,17% | 15,66% |
| RAM mínima | 2,3% | 3,0% | 30,5% |
| RAM máxima | 2,8% | 3,9% | 30,9% |

# 5. Principais Observações

1. **Redis** apresentou o maior throughput em todas as operações criptográficas leves (AES, SHA, HMAC), atingindo até **39.757 ops/s** (INSERT+SHA-256, 64 B), beneficiando-se de sua arquitetura *in-memory*.

2. **MongoDB** apresentou desempenho intermediário e equilibrado, com throughput 2 a 3 vezes superior ao Cassandra na maioria das operações.

3. **Cassandra** foi competitivo para payloads pequenos (até 1.024 B), porém apresentou **colapso de throughput para payloads de 4.096 bytes** em operações de escrita (INSERT e UPDATE) — caindo para ~22,7 ops/s, uma degradação superior a 200x. Esse comportamento **não ocorre em READ e DELETE**, e é atribuído ao mecanismo de *compaction* e ao acúmulo de *tombstones* em implantações *single-node*.

4. **Bcrypt e Argon2** apresentaram throughput praticamente **idêntico nos três bancos** (~20 ops/s e ~30 ops/s, respectivamente), confirmando que essas operações são **estritamente CPU-bound** — a escolha do banco de dados é irrelevante para o desempenho dessas operações específicas.

5. O consumo de **RAM** revelou diferenças arquiteturais marcantes: Redis (2,3%–2,8%) e MongoDB (3,0%–3,9%) mantiveram uso baixo, enquanto Cassandra consumiu consistentemente **mais de 30%** dos 32 GB disponíveis, refletindo o *footprint* da JVM.
