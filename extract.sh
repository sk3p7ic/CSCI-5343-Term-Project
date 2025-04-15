#!/bin/bash

echo ">>> Removing old files, if present."
rm -rf tests/*
rm -rf prompts/*

echo ">>> Ensuring dataset file is downloaded."
filename="dataset_with_difficulty_and_algorithm.json"
if [ ! -f "$filename" ]; then
    wget "https://github.com/huangd1999/EffiBench/raw/refs/heads/main/data/$filename"
fi


echo ">>> Running extractor script."
deno --allow-write ./dataset_extractor.ts
rm "$filename"

echo ">>> Running tests."
cd tests
for fname in *tests*.py; do
    if [ -f "$fname" ]; then
        echo "Running $fname"
        python3 "$fname" test
    fi
done

#echo ">>> Gathering average execution times."
#for fname in *tests*.py; do
#    if [ -f "$fname" ]; then
#        echo "Running $fname"
#        python3 "$fname" time 1000
#    fi
#done