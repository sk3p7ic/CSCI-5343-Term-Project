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
for fname in *tests*.py; do
    if [ -f "$fname" ]; then
        echo "Running all in $fname"
        python3 "$fname" test all
    fi
done

echo ">>> Gathering average execution times."
for fname in *tests*.py; do
    if [ -f "$fname" ]; then
        echo "Running $fname"
        python3 "$fname" time canon 10 >> ../res.txt
        python3 "$fname" time chatgpt 10 >> ../res.txt
        python3 "$fname" time claude 10 >> ../res.txt
        python3 "$fname" time gemini 10 >> ../res.txt
    fi
done