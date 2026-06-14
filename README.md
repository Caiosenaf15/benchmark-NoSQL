# Reprodutibilidade

## Benchmark do Impacto de Mecanismos Criptográficos em Bancos de Dados NoSQL

Este repositório contém todo o material necessário para reproduzir os experimentos realizados no estudo sobre o impacto de mecanismos criptográficos no desempenho de bancos de dados NoSQL.

O benchmark avalia o custo computacional introduzido por técnicas de criptografia, hashing e autenticação quando integradas às operações de inserção, leitura, atualização e remoção de dados.

---

# Visão Geral

A proteção de informações sensíveis é um requisito fundamental em sistemas modernos. Entretanto, a aplicação de mecanismos criptográficos pode introduzir sobrecarga computacional e impactar o desempenho dos bancos de dados.

Este benchmark foi desenvolvido para analisar esse impacto em diferentes bancos de dados NoSQL utilizando algoritmos amplamente empregados na indústria.

## Bancos de Dados Avaliados

* MongoDB
* Redis
* Apache Cassandra

## Algoritmos Avaliados

### Criptografia

* AES-256

### Hash

* SHA-256
* bcrypt
* Argon2

### Autenticação

* HMAC-SHA256

---

# Ambiente Experimental

## Hardware

| Componente     | Especificação        |
| -------------- | -------------------- |
| Processador    | Intel Core i5-12400F |
| Memória RAM    | 32 GB DDR4           |
| Placa de Vídeo | NVIDIA RTX 4060      |
| Armazenamento  | SSD                  |

## Sistema Operacional

| Componente          | Versão                         |
| ------------------- | ------------------------------ |
| Sistema Operacional | Debian GNU/Linux 12 (Bookworm) |
| Kernel Linux        | 6.x                            |

---

# Versões dos Softwares

| Software  | Versão |
| --------- | ------ |
| Python    | 3.x    |
| Java      | 21     |
| MongoDB   | 7.x    |
| Redis     | 7.x    |
| Cassandra | 5.x    |
| YCSB      | 0.17.0 |

---

# Escopo do Benchmark

O benchmark avalia operações criptográficas aplicadas diretamente às operações de banco de dados.

## Operações de Criptografia

* Criptografia AES-256
* Descriptografia AES-256

## Operações de Hash

* SHA-256
* bcrypt
* Argon2

## Operações de Autenticação

* HMAC-SHA256

---

# Operações Avaliadas

| Operação                | Descrição                          |
| ----------------------- | ---------------------------------- |
| insert_aes256           | Criptografar e inserir registro    |
| insert_sha256           | Gerar hash SHA-256 e inserir       |
| insert_hmac_sha256      | Gerar HMAC e inserir               |
| insert_bcrypt           | Gerar hash bcrypt e inserir        |
| insert_argon2           | Gerar hash Argon2 e inserir        |
| read_decrypt_aes256     | Ler e descriptografar              |
| read_verify_sha256      | Ler e verificar hash               |
| update_reencrypt_aes256 | Atualizar e criptografar novamente |
| delete_encrypted_record | Remover registro criptografado     |

---

# Geração das Cargas de Trabalho

Os testes utilizam o framework YCSB (Yahoo! Cloud Serving Benchmark), amplamente utilizado para avaliação de desempenho em bancos de dados.

## Versão

* YCSB 0.17.0

## Workloads Utilizados

### Workload A

* 50% Leituras
* 50% Atualizações

### Workload B

* 95% Leituras
* 5% Atualizações

### Workload C

* 100% Leituras

### Workload D

* Read Latest

---

# Dados Utilizados

Nenhum conjunto de dados externo foi utilizado nos experimentos finais.

Todos os registros utilizados nos testes foram gerados e manipulados pelo YCSB.

Os resultados apresentados neste trabalho foram produzidos exclusivamente a partir dos workloads padronizados fornecidos pelo YCSB.

---

# Estrutura do Repositório

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
│
├── redis/
│
├── cassandra/
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

# Instalação

## Linux

Atualize os pacotes:

```bash
sudo apt update
```

Instale as dependências:

```bash
sudo apt install python3 python3-pip openjdk-21-jdk git
```

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>

cd benchmark
```

Instale as dependências Python:

```bash
pip install -r requirements.txt
```

---

## Windows

Recomenda-se:

* Docker Desktop
* WSL2 (Ubuntu)

Instale:

* Python 3.x
* Java 21
* Git

Clone o repositório:

```powershell
git clone <URL_DO_REPOSITORIO>

cd benchmark
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

---

# Execução dos Testes

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

Para executar todos os testes:

```bash
./scripts/run_all.sh
```

---

# Coleta das Informações do Sistema

Para registrar as características do ambiente utilizado:

```bash
./scripts/collect_system_info.sh
```

As seguintes informações serão coletadas:

* Processador
* Memória RAM
* Sistema Operacional
* Kernel Linux
* Armazenamento

---

# Arquivos Gerados

Após a execução dos testes, espera-se a geração dos seguintes arquivos:

```text
results/

├── mongodb_results.json
├── redis_results.json
├── cassandra_results.json
├── system_info.txt
└── benchmark_summary.csv
```

---

# Validação dos Resultados

Para verificar se os testes foram executados corretamente:

```bash
python scripts/validate_results.py
```

Saída esperada:

```text
PASS

Todos os benchmarks foram executados com sucesso.
```

---

# Checklist de Reprodutibilidade

* [ ] Repositório clonado
* [ ] Dependências instaladas
* [ ] Java instalado
* [ ] Python instalado
* [ ] MongoDB configurado
* [ ] Redis configurado
* [ ] Cassandra configurado
* [ ] YCSB configurado
* [ ] Benchmark executado
* [ ] Resultados gerados
* [ ] Resultados validados

---

# Limitações

Os resultados podem variar em função de:

* Processador utilizado
* Quantidade de memória disponível
* Tipo de armazenamento
* Sistema operacional
* Processos executando em segundo plano

Apesar disso, as tendências de desempenho observadas devem permanecer consistentes.

---

# Como Citar

Caso utilize este benchmark em pesquisas futuras, cite:

```bibtex
@misc{benchmark_nosql_criptografia,
  title={Benchmark do Impacto de Mecanismos Criptográficos em Bancos de Dados NoSQL},
  author={Autores},
  year={2026}
}
```

---

# Contato

Em caso de dúvidas sobre a implementação, execução ou reprodução dos experimentos, entre em contato com os autores do trabalho.
