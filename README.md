# Reprodutibilidade

# Benchmark do Impacto de Mecanismos Criptográficos em Bancos de Dados NoSQL

## Pacote de Reprodutibilidade

Este repositório contém os artefatos necessários para reproduzir os experimentos realizados no artigo sobre o impacto de mecanismos criptográficos no desempenho de bancos de dados NoSQL.

O objetivo do estudo é avaliar o custo computacional introduzido por algoritmos de criptografia, hashing e autenticação quando aplicados a operações comuns de armazenamento e recuperação de dados.

---

# Visão Geral

A proteção de informações sensíveis é um requisito fundamental em sistemas modernos. Entretanto, mecanismos criptográficos podem introduzir sobrecarga computacional e impactar o desempenho dos sistemas de armazenamento.

Este benchmark foi desenvolvido para medir esse impacto em diferentes bancos de dados NoSQL utilizando algoritmos amplamente empregados em aplicações reais.

---

# Bancos de Dados Avaliados

- MongoDB
- Redis
- Apache Cassandra

---

# Algoritmos Avaliados

## Criptografia

- AES-256

## Hash

- SHA-256
- bcrypt
- Argon2

## Autenticação

- HMAC-SHA256

---

# Operações Avaliadas

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

# Configuração Experimental

## Benchmark Criptográfico

### Iterações

10000 execuções por operação.

### Tamanhos dos Dados

- 64 bytes
- 256 bytes
- 1024 bytes
- 4096 bytes

### Métricas Coletadas

- Throughput (operações por segundo)
- Tempo médio de execução
- Latência

---

# Benchmark YCSB

Além dos benchmarks criptográficos personalizados, foi utilizado o Yahoo! Cloud Serving Benchmark (YCSB) para avaliar os bancos sob cargas de trabalho padronizadas.

## Ferramenta

- YCSB 0.17.0

## Configuração

```text
operationcount=100000
```

Os workloads utilizados foram os workloads padrão disponibilizados pelo projeto YCSB.

Repositório oficial:

https://github.com/brianfrankcooper/YCSB

---

# Ambiente Experimental

## Hardware

| Componente | Especificação |
|------------|--------------|
| Processador | Intel Core i5-12400F |
| Memória RAM | 32 GB DDR4 |
| Placa de Vídeo | NVIDIA GeForce RTX 4060 |
| Armazenamento | SSD |
| Arquitetura | x86_64 |

## Sistema Operacional

| Componente | Versão |
|------------|---------|
| Sistema Operacional | Debian GNU/Linux 12 (Bookworm) |

---

# Softwares Utilizados

| Software | Versão |
|-----------|---------|
| Python | 3.x |
| Java | 21 |
| MongoDB | 7.x |
| Redis | 7.x |
| Apache Cassandra | 5.x |
| YCSB | 0.17.0 |

---

# Estrutura do Repositório

```text
benchmark-NoSQL/

README.md
LICENSE
requirements.txt

scripts/

mongodb/

redis/

cassandra/

results/

docs/
```

---

# Instalação

## Linux

Clone o repositório:

```bash
git clone https://github.com/Caiosenaf15/benchmark-NoSQL.git

cd benchmark-NoSQL
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Windows

Instale:

- Python 3.x
- Java 21
- Git

Clone o repositório:

```powershell
git clone https://github.com/Caiosenaf15/benchmark-NoSQL.git

cd benchmark-NoSQL
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

---

# Execução dos Experimentos

## MongoDB

```bash
python mongodb/benchmark.py
```

## Redis

```bash
python redis/benchmark.py
```

## Cassandra

```bash
python cassandra/benchmark.py
```

---

# Execução Completa

Caso o script esteja disponível:

```bash
bash scripts/run_all.sh
```

---

# Resultados

Os resultados gerados pelos experimentos encontram-se na pasta:

```text
results/
```

Os arquivos incluem:

- Resultados dos benchmarks criptográficos
- Resultados do YCSB
- Arquivos JSON de saída
- Métricas de desempenho utilizadas no artigo

---

# Documentação

Documentos complementares disponíveis em:

```text
docs/

metodologia.pdf
hardware.pdf
resultados.pdf
```

Esses documentos descrevem:

- Metodologia experimental
- Configuração do ambiente
- Organização e interpretação dos resultados

---

# Reprodutibilidade

Todos os scripts utilizados para gerar os resultados apresentados no artigo estão disponíveis neste repositório.

Os resultados brutos utilizados para produzir tabelas, gráficos e análises também estão disponíveis para consulta.

Pequenas variações podem ocorrer devido a diferenças de hardware, sistema operacional ou carga da máquina durante a execução dos testes.

Entretanto, as tendências observadas devem permanecer consistentes.

---

# Limitações

Os resultados podem variar em função de:

- Processador utilizado
- Quantidade de memória disponível
- Tipo de armazenamento
- Sistema operacional
- Processos executados em segundo plano

---

# Licença

Este projeto está disponibilizado para fins acadêmicos e de pesquisa.

Consulte o arquivo LICENSE para mais informações.

---

# Autores

Caio Sena

CEFET-RJ

Curso de Sistemas de Informação

2026

Em caso de dúvidas sobre a implementação, execução ou reprodução dos experimentos, entre em contato com os autores do trabalho.
