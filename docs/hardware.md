# Ambiente Experimental

## Hardware

Os experimentos foram executados em uma máquina dedicada com a seguinte configuração:

| Componente | Especificação |
|------------|--------------|
| Processador | Intel Core i5-12400F |
| Núcleos | 6 núcleos físicos / 12 threads |
| Memória RAM | 32 GB DDR4 |
| Placa de Vídeo | NVIDIA GeForce RTX 4060 |
| Armazenamento | SSD |
| Arquitetura | x86_64 |

---

## Sistema Operacional

| Componente | Versão |
|------------|---------|
| Sistema Operacional | Debian GNU/Linux 12 (Bookworm) |
| Kernel Linux | 6.x |

---

## Softwares Utilizados

### Linguagens e Runtime

| Software | Versão |
|-----------|---------|
| Python | 3.x |
| Java | 21 |

### Bancos de Dados

| Banco | Versão |
|--------|---------|
| MongoDB | 7.x |
| Redis | 7.x |
| Apache Cassandra | 5.x |

### Ferramentas

| Ferramenta | Versão |
|------------|---------|
| YCSB | 0.17.0 |

---

## Configuração dos Bancos

### MongoDB

- Instalação local
- Configuração padrão
- Execução standalone

### Redis

- Instalação local
- Configuração padrão
- Execução standalone

### Apache Cassandra

- Instalação local
- Cluster de nó único

---

## Observações

Os resultados podem variar de acordo com:

- Processador utilizado
- Quantidade de memória disponível
- Tipo de armazenamento
- Sistema operacional
- Processos executados em segundo plano

Entretanto, as tendências observadas durante os experimentos devem permanecer consistentes quando reproduzidas em ambientes equivalentes.