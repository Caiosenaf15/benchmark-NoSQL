# Benchmark do Impacto de Mecanismos Criptográficos em Bancos de Dados NoSQL

Site: <https://caiosenaf15.github.io/benchmark-NoSQL/>

## Reprodutibilidade

Este repositório contém os artefatos necessários para reproduzir os experimentos realizados no artigo sobre o impacto de mecanismos criptográficos no desempenho de bancos de dados NoSQL.

O objetivo do estudo é avaliar o custo computacional introduzido por algoritmos de criptografia, hashing e autenticação quando aplicados a operações comuns de armazenamento e recuperação de dados.

---

# Visão Geral

A proteção de informações sensíveis é um requisito fundamental em sistemas modernos. Entretanto, mecanismos criptográficos podem introduzir sobrecarga computacional e impactar o desempenho dos sistemas de armazenamento.

Este benchmark foi desenvolvido para medir esse impacto em diferentes bancos de dados NoSQL utilizando algoritmos amplamente empregados em aplicações reais.

---

# Bancos de Dados Avaliados

- MongoDB 7.0
- Redis 7.x
- Apache Cassandra 4.1

---

# Algoritmos Avaliados

## Criptografia

- AES-256-CFB

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

10.000 execuções por operação, por tamanho de payload.

### Tamanhos dos Dados

- 64 bytes
- 256 bytes
- 1024 bytes
- 4096 bytes

### Métricas Coletadas

- Throughput (operações por segundo)
- Tempo médio de execução (latência, ms/op)
- Uso médio e de pico de CPU (%)
- Uso médio e de pico de RAM (%)

Amostragem de CPU/RAM realizada em thread separada, a cada 50 ms, durante a execução de cada teste.

---

# Benchmark YCSB

Além dos benchmarks criptográficos personalizados, foi utilizado o Yahoo! Cloud Serving Benchmark (YCSB) para avaliar os bancos sob cargas de trabalho padronizadas.

## Ferramenta

- YCSB 0.17.0

## Configuração
recordcount=100000      (fase de load)

operationcount=100000   (fase de execução)

Workloads utilizados: A, B, C e D (workloads padrão disponibilizados pelo projeto YCSB).

Repositório oficial: <https://github.com/brianfrankcooper/YCSB>

---

# Ambiente Experimental

## Hardware

| Componente     | Especificação                                                                |
| -------------- | ----------------------------------------------------------------------------- |
| Processador    | Intel Core i5-12400F (12ª geração, 6 núcleos físicos / 12 threads, 800 MHz–5.600 MHz) |
| Memória RAM    | 32 GB DDR4                                                                     |
| Placa de Vídeo | NVIDIA GeForce RTX 4060                                                        |
| Armazenamento  | 3 HDs físicos dedicados (um banco por disco)                                   |
| Arquitetura    | x86_64                                                                         |

> Cada SGBD foi instalado em um **disco físico exclusivo**, na mesma máquina, para eliminar a interferência de I/O compartilhado entre os bancos durante os testes — uma decisão metodológica central deste estudo.

## Sistema Operacional

| Componente          | Versão                                  |
| ------------------- | ----------------------------------------- |
| Sistema Operacional | Debian GNU/Linux 12 (Bookworm), kernel 6.1.0-48-amd64 |

---

# Softwares Utilizados

| Software          | Versão                              |
| ------------------ | ------------------------------------- |
| Python             | 3.11                                   |
| Java (Cassandra)   | OpenJDK 11.0.2 (instalação manual)     |
| MongoDB            | 7.0                                     |
| Redis              | 7.x (repositório Debian Bookworm)      |
| Apache Cassandra   | 4.1.x (repositório apache.org, série 41x) |
| YCSB               | 0.17.0                                  |

> **Importante:** o Apache Cassandra 4.1 **não é compatível com Java 17+** (gera erros `InaccessibleObjectException` e falhas com opções CMS). Foi necessário instalar o **OpenJDK 11.0.2** manualmente a partir do binário oficial (`jdk-11.0.2_linux-x64_bin.tar.gz`, download.java.net) e configurar `JAVA_HOME` apontando para `/opt/jdk-11.0.2`. Veja a seção **Troubleshooting** abaixo.

---

# Estrutura do Repositório
benchmark-NoSQL/

├── README.md

├── LICENSE

├── requirements.txt

├── index.html

├── cassandra/

├── mongodb/

├── redis/

├── scripts/

├── src/

│   └── CEFETRJ.png

├── results/

│   ├── crypto_benchmark_redis_20260523_203720.json

│   ├── crypto_benchmark_mongo_20260523_114130.json

│   ├── crypto_benchmark_cassandra_20260523_135802.json

│   └── README.md

└── docs/

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

## Windows

Instale:

- Python 3.11
- Java (apenas necessário para Cassandra — recomendado Java 11)
- Git

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

# Instalação dos Bancos de Dados (Debian 12)

## Comum a todos os ambientes

```bash
dpkg --configure -a && apt update && apt upgrade -y
apt install -y python3 python3-pip wget curl default-jdk maven
pip3 install pymongo redis cassandra-driver cryptography psutil bcrypt argon2-cffi --break-system-packages

cd /root
wget https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-0.17.0.tar.gz
tar xzf ycsb-0.17.0.tar.gz && mv ycsb-0.17.0 ycsb
ln -s /usr/bin/python3 /usr/bin/python
mkdir -p /root/benchmark/results /root/benchmark/data
```

## MongoDB 7.0

```bash
apt install -y gnupg
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" > /etc/apt/sources.list.d/mongodb-org-7.0.list
apt update && apt install -y mongodb-org
systemctl enable mongod && systemctl start mongod
```

## Redis

```bash
apt update && apt install -y redis-server
systemctl enable redis-server && systemctl start redis-server
```

## Apache Cassandra 4.1 (com Java 11)

```bash
echo "deb https://debian.cassandra.apache.org 41x main" > /etc/apt/sources.list.d/cassandra.sources.list
curl https://downloads.apache.org/cassandra/KEYS | apt-key add -
apt update && apt install -y cassandra
```

Após instalar, configure o Java 11 conforme a seção **Troubleshooting**, e inicie com:

```bash
JAVA_HOME=/opt/jdk-11.0.2 cassandra -R
```

---

# Execução dos Experimentos

Edite o `config.py` correspondente e defina `DB_TARGET` como `"mongodb"`, `"redis"` ou `"cassandra"`.

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

Os resultados gerados pelos experimentos encontram-se na pasta `results/`:

- `crypto_benchmark_redis_20260523_203720.json`
- `crypto_benchmark_mongo_20260523_114130.json`
- `crypto_benchmark_cassandra_20260523_135802.json`

Cada arquivo contém, por tamanho de payload (64, 256, 1024 e 4096 bytes) e por operação, as métricas de throughput, latência média, uso médio/pico de CPU e RAM.

---

# Documentação

Documentos complementares disponíveis em `docs/`:

- Metodologia experimental
- Configuração do ambiente (hardware e software)
- Organização e interpretação dos resultados

---

# Troubleshooting

Esta seção documenta os principais problemas enfrentados durante a instalação e configuração dos ambientes, e como foram resolvidos. Eles podem se repetir em tentativas de reprodução deste experimento.

## Instalação do Debian

O **Secure Boot** deve ser **desativado na BIOS** antes de instalar o Debian (erro comum: `SBAT self-check failed`).

Durante a instalação, é **crítico desmarcar os ambientes gráficos** (GNOME, Xfce) e selecionar apenas **"servidor SSH"** e **"utilitários padrão do sistema"**. Caso o ambiente gráfico seja instalado por engano, ele pode ser removido com:

```bash
apt remove --purge gnome* xfce4* lightdm gdm3 -y
apt autoremove --purge -y
systemctl set-default multi-user.target
reboot
```

## Apache Cassandra 4.1 + Java

Cassandra 4.1 **não roda como root sem a flag `-R`**:

```bash
cassandra -R -f
```

Cassandra 4.1 é **incompatível com Java 17** (erros de opções CMS e `InaccessibleObjectException: module java.base does not "opens java.io"`). A solução foi instalar o **Java 11** manualmente:

```bash
# baixar jdk-11.0.2_linux-x64_bin.tar.gz de download.java.net
tar xzf jdk-11.0.2_linux-x64_bin.tar.gz -C /opt/

export JAVA_HOME=/opt/jdk-11.0.2
export PATH=$JAVA_HOME/bin:$PATH
echo 'export JAVA_HOME=/opt/jdk-11.0.2' >> /root/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /root/.bashrc
echo 'export JAVA_HOME=/opt/jdk-11.0.2' >> /etc/cassandra/cassandra-env.sh
```

Para iniciar o Cassandra em segundo plano (não usar `Ctrl+Z`, que apenas pausa o processo):

```bash
JAVA_HOME=/opt/jdk-11.0.2 cassandra -R
# aguardar ~2 minutos e testar com:
cqlsh
```

Se o `dpkg` for interrompido após um reboot forçado:

```bash
dpkg --configure -a
```

## YCSB com Cassandra

Antes de rodar o `load`, é necessário criar manualmente o keyspace e a tabela:

```bash
cqlsh -e "CREATE KEYSPACE IF NOT EXISTS ycsb WITH replication = {'class':'SimpleStrategy','replication_factor':'1'};"
cqlsh -e "CREATE TABLE IF NOT EXISTS ycsb.usertable (y_id varchar PRIMARY KEY, field0 varchar, field1 varchar, field2 varchar, field3 varchar, field4 varchar, field5 varchar, field6 varchar, field7 varchar, field8 varchar, field9 varchar);"
```

## Dataset RT-IoT2022

O dataset RT-IoT2022 do UCI Machine Learning Repository exige login para download direto (tentativas via `wget`/`curl` retornam 0–14 bytes). Alternativas:

- Baixar via Kaggle em outra máquina e transferir por pendrive;
- Ou acessar manualmente em: <https://archive.ics.uci.edu/dataset/942/rt-iot2022>

Nos testes de criptografia, os payloads utilizados foram gerados de forma sintética via `os.urandom()`, eliminando a dependência direta do dataset para as métricas de desempenho criptográfico (o dataset foi usado apenas para a etapa de importação inicial / massa de dados realista).

## Comando `wget` com flag incorreta

Ao copiar comandos de fontes diversas, atenção: `wget -O arquivo url` usa "O" maiúsculo, não "0" (zero) — erro comum de digitação. Prefira:

```bash
curl -L -o arquivo url
```

---

# Reprodutibilidade

Todos os scripts utilizados para gerar os resultados apresentados no artigo estão disponíveis neste repositório.

Os resultados brutos utilizados para produzir tabelas, gráficos e análises também estão disponíveis para consulta em `results/`.

Pequenas variações podem ocorrer devido a diferenças de hardware, sistema operacional ou carga da máquina durante a execução dos testes. Entretanto, as tendências observadas devem permanecer consistentes.

---

# Limitações

Os resultados podem variar em função de:

- Processador utilizado
- Quantidade de memória disponível
- Tipo de armazenamento
- Sistema operacional
- Processos executados em segundo plano

Adicionalmente:

- Os experimentos foram realizados em implantação **single-node** (sem cluster), portanto os resultados do Cassandra não refletem seu desempenho em cluster distribuído, cenário para o qual foi projetado.
- A execução foi **serial** (sem concorrência de múltiplas threads de cliente nos benchmarks de criptografia).
- O **Redis** foi configurado **sem persistência em disco** (`save ""`), o que favorece seu throughput em comparação com configurações de produção que exigem durabilidade.

---

# Licença

Este projeto está disponibilizado para fins acadêmicos e de pesquisa. Consulte o arquivo `LICENSE` (MIT) para mais informações.

---

# Citação

```bibtex
@article{benchmark_nosql_crypto_2026,
  title={Benchmark do Impacto de Mecanismos Criptográficos em Bancos de Dados NoSQL},
  author={Sena Freitas, Caio and Tavares Pinto, Pedro Henrique},
  year={2026},
  institution={CEFET/RJ - Unidade de Ensino Descentralizada de Nova Friburgo}
}
```

---

# Autores

**Caio Sena Freitas** e **Pedro Henrique T. Pinto**
CEFET/RJ — Curso de Sistemas de Informação
2026

Em caso de dúvidas sobre a implementação, execução ou reprodução dos experimentos, entre em contato com os autores do trabalho.
