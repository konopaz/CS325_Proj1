#!/bin/bash
echo "packing up deliverables into zip file..."

rm -Rf Group24Project1.zip
rm -Rf Group24Project1

mkdir -p Group24Project1
cp README.md Group24Project1/
cp algorithms.py Group24Project1/
cp benchmark.py Group24Project1/
cp problems.py Group24Project1/
cp dataruns.sh Group24Project1/
cp test-problems.txt Group24Project1/
cp test-solutions.txt Group24Project1/
cp MSS_Problems.txt Group24Project1/
cp MSS_Results.txt Group24Project1/
cp package.sh Group24Project1/

zip -r Group24Project1.zip Group24Project1

rm -Rf Group24Project1
