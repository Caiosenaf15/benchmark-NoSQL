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

## Hardware

| Componente     | Especificação                                  |
| --------------- | ------------------------------------------------ |
| Processador     | Intel Core i5-12400F (12ª geração, 6 núcleos / 12 threads, 800 MHz–5.600 MHz) |
| Memória RAM     | 32 GB DDR4                                        |
| Placa de Vídeo  | NVIDIA GeForce RTX 4060                           |
| Armazenamento   | 3 HDs físicos dedicados (1 por banco de dados)    |
| Arquitetura     | x86_64                                            |

> Cada SGBD foi instalado em um **disco físico exclusivo**, sob a mesma máquina,
> para eliminar a interferência de I/O compartilhado entre os bancos durante os
> testes — uma decisão metodológica central deste estudo.

## Sistema Operacional

| Componente | Versão |
|------------|---------|
| Sistema Operacional | Debian GNU/Linux 12 (Bookworm) |

---

# Softwares Utilizados

| Software         | Versão                          |
| ---------------- | -------------------------------- |
| Python           | 3.11                              |
| Java (Cassandra) | OpenJDK 11.0.2 (instalação manual) |
| MongoDB          | 7.0                                |
| Redis            | 7.x (repositório Debian Bookworm) |
| Apache Cassandra | 4.1.x (apache.org 41x)            |
| YCSB             | 0.17.0                            |

> **Nota importante:** o Apache Cassandra 4.1 **não é compatível com Java 17+**
> (gera erros `InaccessibleObjectException` e falhas com opções CMS). Foi necessário
> instalar o **OpenJDK 11.0.2** manualmente a partir do binário oficial
> (`jdk-11.0.2_linux-x64_bin.tar.gz`, download.java.net) e configurar `JAVA_HOME`
> apontando para `/opt/jdk-11.0.2`. Veja a seção **Troubleshooting** abaixo.

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

# Troubleshooting

Esta seção documenta os principais problemas enfrentados durante a instalação
e configuração dos ambientes, e como foram resolvidos. Eles podem se repetir
em tentativas de reprodução deste experimento.

## Instalação do Debian

- O **Secure Boot** deve ser **desativado na BIOS** antes de instalar o Debian
  (erro comum: `SBAT self-check failed`).
- Durante a instalação, é **crítico desmarcar os ambientes gráficos** (GNOME,
  Xfce) e selecionar apenas **"servidor SSH"** e **"utilitários padrão do
  sistema"**. Caso o ambiente gráfico seja instalado por engano, ele pode ser
  removido com:

```bash
apt remove --purge gnome* xfce4* lightdm gdm3 -y
apt autoremove --purge -y
systemctl set-default multi-user.target
reboot
```

## Apache Cassandra 4.1 + Java

- Cassandra 4.1 **não roda como root sem a flag `-R`**:

```bash
cassandra -R -f
```

- Cassandra 4.1 é **incompatível com Java 17** (erros de opções CMS e
  `InaccessibleObjectException: module java.base does not "opens java.io"`).
  A solução foi instalar o **Java 11** manualmente:

```bash
# baixar jdk-11.0.2_linux-x64_bin.tar.gz de download.java.net
tar xzf jdk-11.0.2_linux-x64_bin.tar.gz -C /opt/

export JAVA_HOME=/opt/jdk-11.0.2
export PATH=$JAVA_HOME/bin:$PATH
echo 'export JAVA_HOME=/opt/jdk-11.0.2' >> /root/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /root/.bashrc
echo 'export JAVA_HOME=/opt/jdk-11.0.2' >> /etc/cassandra/cassandra-env.sh
```

- Para iniciar o Cassandra em segundo plano (não usar `Ctrl+Z`, que apenas
  pausa o processo):

```bash
JAVA_HOME=/opt/jdk-11.0.2 cassandra -R
# aguardar ~2 minutos e testar com:
cqlsh
```

- Se o `dpkg` for interrompido após um reboot forçado:

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

O dataset RT-IoT2022 do UCI Machine Learning Repository exige login para
download direto (tentativas via `wget`/`curl` retornam 0–14 bytes). Alternativas:

- Baixar via Kaggle em outra máquina e transferir por pendrive;
- Ou acessar manualmente em: https://archive.ics.uci.edu/dataset/942/rt-iot2022

Nos testes de criptografia, os payloads utilizados foram gerados de forma
sintética via `os.urandom()`, eliminando a dependência direta do dataset
para as métricas de desempenho criptográfico (o dataset foi usado apenas
para a etapa de importação inicial / massa de dados realista).

## Comando `wget` com flag incorreta

Ao copiar comandos de fontes diversas, atenção: `wget -O arquivo url` usa
"O" maiúsculo, não "0" (zero) — erro comum de digitação. Prefira:

```bash
curl -L -o arquivo url
```
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
e
Pedro Henrique Tavares

CEFET-RJ

Curso de Sistemas de Informação

2026

Em caso de dúvidas sobre a implementação, execução ou reprodução dos experimentos, entre em contato com os autores do trabalho.
