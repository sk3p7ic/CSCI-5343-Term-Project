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
epochs=100000
rm ../*.bak
mv ../times.csv ../times.csv.bak
for fname in *tests*.py; do
    if [ -f "$fname" ]; then
        echo "Running $fname"
        python3 "$fname" time canon "$epochs" >> ../times.csv
        python3 "$fname" time chatgpt "$epochs" >> ../times.csv
        python3 "$fname" time claude "$epochs" >> ../times.csv
        python3 "$fname" time gemini "$epochs" >> ../times.csv
    fi
done

cd ..
python3 time_printer.py
