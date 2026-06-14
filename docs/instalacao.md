# Instalação dos Bancos de Dados (Debian 12)

## Comum a todos os HDs

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

Após instalar, configure o Java 11 conforme a seção **Troubleshooting**, e
inicie com:

```bash
JAVA_HOME=/opt/jdk-11.0.2 cassandra -R
```