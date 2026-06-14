#!/bin/bash

mkdir -p results

OUTPUT="results/system_info.txt"

echo "===== CPU =====" > $OUTPUT
lscpu >> $OUTPUT

echo "" >> $OUTPUT
echo "===== MEMÓRIA =====" >> $OUTPUT
free -h >> $OUTPUT

echo "" >> $OUTPUT
echo "===== DISCO =====" >> $OUTPUT
lsblk >> $OUTPUT

echo "" >> $OUTPUT
echo "===== SISTEMA =====" >> $OUTPUT
uname -a >> $OUTPUT

echo "" >> $OUTPUT
echo "===== PYTHON =====" >> $OUTPUT
python3 --version >> $OUTPUT

echo "" >> $OUTPUT
echo "===== JAVA =====" >> $OUTPUT
java --version >> $OUTPUT