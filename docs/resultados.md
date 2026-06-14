# Resultados

Este documento descreve os arquivos de resultados disponibilizados neste repositório e explica como interpretar as métricas coletadas durante os experimentos.

---

# Organização dos Resultados

Todos os resultados gerados pelos benchmarks estão armazenados no diretório:

```text
results/
```

Os arquivos estão divididos em duas categorias:

1. Benchmarks criptográficos
2. Benchmarks YCSB

---

# Benchmarks Criptográficos

Os benchmarks criptográficos avaliam o impacto dos algoritmos de criptografia, hashing e autenticação nas operações de banco de dados.

Arquivos:

```text
crypto_benchmark_mongo_*.json
crypto_benchmark_redis_*.json
crypto_benchmark_cassandra_*.json
```

Cada arquivo contém os resultados obtidos para um banco de dados específico.

---

## Operações Avaliadas

### Inserção

- insert_aes256
- insert_sha256
- insert_hmac_sha256
- insert_bcrypt
- insert_argon2

### Leitura

- read_decrypt_aes256
- read_verify_sha256

### Atualização

- update_reencrypt_aes256

### Remoção

- delete_encrypted_record

---

## Tamanhos dos Dados

Os testes foram realizados utilizando payloads de:

- 64 bytes
- 256 bytes
- 1024 bytes
- 4096 bytes

---

## Métricas Coletadas

### Tempo Médio

Tempo médio necessário para concluir uma operação.

Unidade:

```text
ms
```

---

### Throughput

Quantidade de operações executadas por segundo.

Unidade:

```text
ops/sec
```

---

### Latência

Tempo necessário para executar uma única operação.

Unidade:

```text
ms
```

---

# Benchmarks YCSB

Os benchmarks YCSB foram utilizados para avaliar o comportamento dos bancos sob cargas de trabalho padronizadas.

Arquivos:

```text
ycsb_A_mongo.txt
ycsb_B_mongo.txt
ycsb_C_mongo.txt
ycsb_D_mongo.txt

ycsb_A_redis.txt
ycsb_B_redis.txt
ycsb_C_redis.txt
ycsb_D_redis.txt

ycsb_A_cassandra.txt
ycsb_B_cassandra.txt
ycsb_C_cassandra.txt
ycsb_D_cassandra.txt
```

---

# Configuração do YCSB

Versão utilizada:

```text
0.17.0
```

Quantidade de operações:

```text
100000
```

---

# Workloads Utilizados

## Workload A

Mistura equilibrada entre leitura e atualização.

```text
50% Read
50% Update
```

---

## Workload B

Predominância de leitura.

```text
95% Read
5% Update
```

---

## Workload C

Somente leitura.

```text
100% Read
```

---

## Workload D

Leitura dos registros mais recentes.

```text
Read Latest
```

---

# Métricas YCSB

Os arquivos de saída do YCSB contêm as seguintes métricas.

---

## Throughput

Número de operações processadas por segundo.

Exemplo:

```text
[OVERALL], Throughput(ops/sec), 103199.17
```

---

## Tempo Total

Tempo necessário para concluir toda a carga de trabalho.

Exemplo:

```text
[OVERALL], RunTime(ms), 969
```

---

## Latência Média

Tempo médio de resposta das operações.

Exemplo:

```text
[READ], AverageLatency(us), 9.21
```

---

## Latência Máxima

Maior latência observada durante a execução.

Exemplo:

```text
[READ], MaxLatency(us), 3799
```

---

## Percentis

Os percentis indicam a distribuição das latências observadas.

Exemplos:

```text
95thPercentileLatency
99thPercentileLatency
```

Esses valores representam o limite abaixo do qual se encontram 95% e 99% das operações executadas.

---

# Interpretação dos Resultados

Ao comparar diferentes bancos de dados, devem ser observados principalmente:

- Throughput
- Latência média
- Latência máxima
- Percentil 95
- Percentil 99

Maior throughput indica maior capacidade de processamento.

Menores latências indicam melhor tempo de resposta.

---

# Resultados Utilizados no Trabalho

Os resultados apresentados no artigo/TCC foram obtidos diretamente a partir dos arquivos disponibilizados neste diretório.

Todos os gráficos, tabelas e análises podem ser reproduzidos utilizando os dados brutos fornecidos.

---

# Reprodutibilidade

Qualquer pesquisador pode reproduzir os experimentos executando os scripts disponibilizados neste repositório e comparando os resultados obtidos com os arquivos presentes na pasta `results/`.

Pequenas variações podem ocorrer devido a diferenças de hardware, sistema operacional ou carga do sistema, porém as tendências gerais observadas devem permanecer consistentes.