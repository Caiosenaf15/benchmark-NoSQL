
---

# hardware.md

```markdown
# Ambiente Experimental

## Objetivo

Esta seção documenta o ambiente utilizado durante a execução dos experimentos.

O detalhamento do hardware e software é fundamental para garantir a reprodutibilidade dos resultados e permitir comparações futuras.

---

# Hardware

Os experimentos foram executados em uma máquina dedicada, evitando interferências externas significativas durante a coleta dos dados.

| Componente | Especificação |
|------------|--------------|
| Processador | Intel Core i5-12400F |
| Arquitetura | x86_64 |
| Núcleos Físicos | 6 |
| Threads | 12 |
| Memória RAM | 32 GB DDR4 |
| GPU | NVIDIA GeForce RTX 4060 |
| Armazenamento | SSD |

---

# Sistema Operacional

| Componente | Versão |
|------------|---------|
| Distribuição | Debian GNU/Linux 12 (Bookworm) |
| Kernel Linux | 6.x |

---

# Linguagens e Ferramentas

## Python

Responsável pela implementação dos benchmarks criptográficos e automação dos experimentos.

## Java

Necessário para execução do YCSB.

---

# Bancos de Dados

## MongoDB

Banco orientado a documentos utilizado nos experimentos.

## Redis

Banco chave-valor utilizado para avaliação de cenários de baixa latência.

## Apache Cassandra

Banco distribuído utilizado para avaliação de ambientes escaláveis.

---

# Ferramentas Auxiliares

## Yahoo! Cloud Serving Benchmark (YCSB)

Ferramenta utilizada para geração de cargas de trabalho padronizadas.

Versão utilizada:

```text
0.17.0