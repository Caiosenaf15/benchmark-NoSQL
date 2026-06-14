# Metodologia Experimental

## Objetivo

Este benchmark foi desenvolvido para avaliar o impacto de mecanismos criptográficos no desempenho de bancos de dados NoSQL.

Foram analisados três sistemas amplamente utilizados:

- MongoDB
- Redis
- Apache Cassandra

O objetivo principal é medir o custo computacional introduzido por algoritmos de criptografia, hashing e autenticação quando aplicados a operações comuns de persistência de dados.

---

## Algoritmos Avaliados

Foram avaliados os seguintes mecanismos criptográficos:

### Criptografia

- AES-256

### Hash

- SHA-256
- bcrypt
- Argon2

### Autenticação

- HMAC-SHA256

---

## Operações Avaliadas

As seguintes operações foram implementadas e medidas:

| Operação | Descrição |
|-----------|------------|
| insert_aes256 | Criptografar e inserir dados |
| insert_sha256 | Gerar hash SHA-256 e inserir |
| insert_hmac_sha256 | Gerar HMAC e inserir |
| insert_bcrypt | Gerar hash bcrypt e inserir |
| insert_argon2 | Gerar hash Argon2 e inserir |
| read_decrypt_aes256 | Ler e descriptografar |
| read_verify_sha256 | Ler e verificar hash |
| update_reencrypt_aes256 | Atualizar e criptografar novamente |
| delete_encrypted_record | Remover registro |

---

## Benchmark Criptográfico

Cada operação foi executada múltiplas vezes para reduzir efeitos de variações temporárias do sistema operacional.

### Configuração

- Iterações por teste: 10000
- Execução local
- Banco de dados executando na mesma máquina

### Tamanhos dos Dados

Os seguintes tamanhos de payload foram utilizados:

- 64 bytes
- 256 bytes
- 1024 bytes
- 4096 bytes

As métricas coletadas incluem:

- Tempo médio de execução
- Operações por segundo
- Latência

---

## Benchmark YCSB

Além dos testes criptográficos personalizados, foi utilizado o Yahoo! Cloud Serving Benchmark (YCSB) para avaliar o comportamento dos bancos sob cargas padronizadas.

### Ferramenta

- YCSB 0.17.0

### Configuração

- operationcount=100000

---

## Procedimento Experimental

Para cada banco de dados:

1. Inicialização do serviço.
2. Inserção dos registros necessários.
3. Execução dos benchmarks criptográficos.
4. Execução dos workloads YCSB.
5. Coleta das métricas.
6. Armazenamento dos resultados em arquivos JSON e TXT.

---

## Coleta de Resultados

Os resultados foram armazenados em arquivos JSON e TXT para posterior análise.

As métricas principais consideradas foram:

- Throughput (operações por segundo)
- Latência média
- Latência máxima
- Percentis de latência
- Tempo total de execução

---

## Reprodutibilidade

Todos os códigos-fonte utilizados nos experimentos estão disponíveis neste repositório.

Os resultados apresentados no trabalho podem ser reproduzidos executando os scripts disponibilizados e utilizando as versões dos softwares descritas na documentação.