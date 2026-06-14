#!/bin/bash

echo "=================================="
echo " MongoDB Benchmark"
echo "=================================="
python mongodb/benchmark.py

echo "=================================="
echo " Redis Benchmark"
echo "=================================="
python redis/benchmark.py

echo "=================================="
echo " Cassandra Benchmark"
echo "=================================="
python cassandra/benchmark.py

echo "=================================="
echo " Finalizado"
echo "=================================="