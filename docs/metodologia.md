# Metodologia Experimental

## Introdução

A crescente adoção de bancos de dados NoSQL em aplicações distribuídas e sistemas de grande escala tem aumentado a preocupação com a proteção de dados sensíveis armazenados nesses ambientes.

Embora mecanismos criptográficos sejam amplamente utilizados para garantir confidencialidade, integridade e autenticidade, sua aplicação pode introduzir sobrecarga computacional e impactar diretamente o desempenho do sistema.

Este trabalho investiga quantitativamente esse impacto por meio de uma série de experimentos controlados realizados em diferentes bancos de dados NoSQL.

---

# Objetivo

O objetivo principal deste benchmark é avaliar o custo computacional introduzido por mecanismos criptográficos amplamente utilizados em aplicações modernas.

Os experimentos buscam responder às seguintes questões:

- Qual o impacto da criptografia no throughput dos bancos NoSQL?
- Como algoritmos de hash afetam o tempo de resposta das operações?
- Qual a diferença de desempenho entre mecanismos de autenticação e criptografia?
- Como diferentes bancos de dados reagem à aplicação desses mecanismos?

---

# Bancos de Dados Avaliados

Os experimentos foram realizados utilizando três bancos de dados NoSQL amplamente adotados pela indústria.

## MongoDB

Banco de dados orientado a documentos que utiliza estruturas JSON/BSON para armazenamento dos dados.

## Redis

Banco de dados chave-valor em memória otimizado para baixa latência e alto throughput.

## Apache Cassandra

Banco de dados distribuído orientado a colunas projetado para alta disponibilidade e escalabilidade horizontal.

---

# Mecanismos Criptográficos Avaliados

## Criptografia Simétrica

### AES-256

Utilizado para avaliar o impacto da criptografia de dados antes do armazenamento.

---

## Hash Criptográfico

### SHA-256

Avaliado como mecanismo de integridade dos dados.

### bcrypt

Avaliado como mecanismo de derivação de chaves e armazenamento seguro de credenciais.

### Argon2

Avaliado como alternativa moderna ao bcrypt, projetada para resistência a ataques por hardware especializado.

---

## Autenticação

### HMAC-SHA256

Utilizado para avaliar mecanismos de autenticação e verificação de integridade.

---

# Operações Avaliadas

As operações implementadas simulam cenários comuns encontrados em aplicações reais.

## Inserção

- insert_aes256
- insert_sha256
- insert_hmac_sha256
- insert_bcrypt
- insert_argon2

## Leitura

- read_decrypt_aes256
- read_verify_sha256

## Atualização

- update_reencrypt_aes256

## Remoção

- delete_encrypted_record

---

# Configuração dos Experimentos

## Iterações

Cada operação foi executada 10000 vezes.

A utilização de múltiplas execuções reduz o impacto de variações temporárias do sistema operacional e melhora a confiabilidade estatística dos resultados.

---

## Tamanhos dos Dados

Foram utilizados diferentes tamanhos de payload para avaliar a escalabilidade dos mecanismos criptográficos.

| Payload |
|----------|
| 64 bytes |
| 256 bytes |
| 1024 bytes |
| 4096 bytes |

---

# Avaliação com YCSB

Além dos benchmarks criptográficos personalizados, foi utilizado o Yahoo! Cloud Serving Benchmark (YCSB), uma ferramenta amplamente adotada para avaliação de desempenho de bancos de dados.

## Versão

YCSB 0.17.0

## Configuração

```text
operationcount=100000