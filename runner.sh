#!/bin/bash

echo ">>> Running tests."
cd tests
for fname in *tests*.py; do
    if [ -f "$fname" ]; then
        echo "Running $fname"
        python3 "$fname" test
    fi
done

echo ">>> Running all tests."
cd tests
for fname in *tests*.py; do
    if [ -f "$fname" ]; then
        echo "Running $fname"
        python3 "$fname" test all
    fi
done

#echo ">>> Gathering average execution times."
#for fname in *tests*.py; do
#    if [ -f "$fname" ]; then
#        echo "Running $fname"
#        python3 "$fname" time 1000
#    fi
#done