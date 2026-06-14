---
title: "Ambiente de Hardware e Software"
subtitle: "Benchmark do Impacto de Mecanismos Criptográficos em Bancos de Dados NoSQL"
author: "Caio Sena Freitas e Pedro Henrique T. Pinto — CEFET/RJ, Nova Friburgo"
date: "2026"
---

# 1. Hardware

| Componente     | Especificação |
| --------------- | --------------- |
| Processador     | Intel Core i5-12400F (12ª geração, Alder Lake, 6 núcleos físicos / 12 threads, 800 MHz–5.600 MHz) |
| Cache L3        | 18 MB |
| Memória RAM     | 32 GB DDR4 |
| Placa de Vídeo  | NVIDIA GeForce RTX 4060 |
| Armazenamento   | 3 HDs físicos dedicados (um banco de dados por disco) |
| Arquitetura     | x86_64 |

> Cada SGBD foi instalado em um **disco físico exclusivo**, na mesma máquina, para eliminar a interferência de I/O compartilhado entre os bancos durante os testes — uma decisão metodológica central deste estudo.

# 2. Sistema Operacional

| Componente          | Versão |
| -------------------- | -------- |
| Distribuição        | Debian GNU/Linux 12 (Bookworm) |
| Kernel              | 6.1.0-48-amd64 |

# 3. Softwares e Versões

| Software          | Versão |
| ------------------ | -------- |
| Python             | 3.11 |
| Java (Cassandra)   | OpenJDK 11.0.2 (instalação manual) |
| MongoDB            | 7.0 |
| Redis              | 7.x (repositório Debian Bookworm) |
| Apache Cassandra   | 4.1.x (repositório apache.org, série 41x) |
| YCSB               | 0.17.0 |

# 4. Configuração dos Bancos de Dados

| Banco | Repositório / Origem | Configuração |
|-------|----------------------|---------------|
| MongoDB 7.0 | repo.mongodb.org/apt/debian | Configuração padrão, sem autenticação, journaling ativo |
| Redis 7.x | Repositório Debian Bookworm | Persistência desabilitada (`save ""`), operação puramente em memória |
| Apache Cassandra 4.1 | debian.cassandra.apache.org (41x) | Java 11, fator de replicação 1, SimpleStrategy, compaction padrão |

# 5. Bibliotecas Python

```text
pymongo
redis
cassandra-driver
cryptography
psutil
bcrypt
argon2-cffi
```

# 6. Nota sobre Compatibilidade Java/Cassandra

O Apache Cassandra 4.1 **não é compatível com Java 17+**, apresentando erros de opções CMS e `InaccessibleObjectException: module java.base does not "opens java.io"`. Foi necessário instalar o **OpenJDK 11.0.2** manualmente a partir do binário oficial (`jdk-11.0.2_linux-x64_bin.tar.gz`, download.java.net), com `JAVA_HOME` apontando para `/opt/jdk-11.0.2`.

Detalhes completos de instalação e resolução de problemas estão disponíveis no `README.md` do repositório, na seção **Troubleshooting**.

# 7. Instalação do Sistema Operacional

Durante a instalação do Debian 12, os seguintes pontos foram observados:

- O **Secure Boot** deve ser **desativado na BIOS** (erro comum: `SBAT self-check failed`).
- Particionamento: instalação UEFI forçada, particionamento padrão (ESP + ext4 + swap).
- Espelho utilizado: `debian.c3sl.ufpr.br` (UFPR).
- Seleção de software: **apenas** "servidor SSH" e "utilitários padrão do sistema" — ambientes gráficos (GNOME/Xfce) **não devem ser instalados**.
