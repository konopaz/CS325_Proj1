#!/bin/bash

steps=9
stepsize=1000

mkdir -p dataruns
echo "starting linear run"
./benchmark.py -a=linear --steps ${steps} --stepsize ${stepsize} > dataruns/linear_${steps}x${stepsize}.txt
echo "finished linear, starting divide"
./benchmark.py -a=divide --steps ${steps} --stepsize ${stepsize} > dataruns/divide_${steps}x${stepsize}.txt
echo "finished divide, starting betterenum"
./benchmark.py -a=betterenum --steps ${steps} --stepsize ${stepsize} > dataruns/betterenum_${steps}x${stepsize}.txt
echo "finished betterenum, starting enumeration"
./benchmark.py -a=enumeration --steps ${steps} --stepsize ${stepsize} > dataruns/enumeration_${steps}x${stepsize}.txt
echo "finished enumeration"
