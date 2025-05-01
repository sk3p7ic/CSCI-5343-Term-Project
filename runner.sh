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
rm -r ../mem-profiles
mkdir ../mem-profiles
epochs=100000
rm ../*.bak
mv ../times.csv ../times.csv.bak
echo "problem,author,avg_time,total_time" > ../times.csv
for fname in *tests*.py; do
    if [ -f "$fname" ]; then
        echo "<><><>------ Running $fname ------<><><>"
	memfile="../mem-profiles/$(echo "$fname" | awk -F'_tests' '{print $1}').dat"
        mprof run --output "$memfile" --interval 0.001 "$fname" time canon "$epochs"
        mprof run --output "$memfile" --interval 0.001 "$fname" time chatgpt "$epochs"
        mprof run --output "$memfile" --interval 0.001 "$fname" time claude "$epochs"
        mprof run --output "$memfile" --interval 0.001 "$fname" time gemini "$epochs"
    fi
done

cd ..
python3 time_printer.py
