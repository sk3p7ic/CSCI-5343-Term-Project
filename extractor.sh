#!/bin/bash

copy_llm_python_files() {
    local source_dir="$1"
    local prefix="$2"
    local dest_dir="./tests"

    for file in "$source_dir"/*.py; do
        fname=$(basename "$file")
        new_filename="${prefix}_$fname"

        cp "$file" "$dest_dir/$new_filename"
        echo "Copied $fname to $dest_dir/$new_filename"
    done
}

echo ">>> Removing old files, if present."
rm -rf tests/*
rm -rf prompts/*

echo ">>> Ensuring dataset file is downloaded."
datafile="dataset_with_difficulty_and_algorithm.json"
if [ ! -f "$datafile" ]; then
    wget "https://github.com/huangd1999/EffiBench/raw/refs/heads/main/data/$datafile"
fi


echo ">>> Running extractor script."
python3 dataset_extractor.py
rm "$datafile"

copy_llm_python_files "./ChatGPT 03-mini-high" "chatgpt"
copy_llm_python_files "./Claude 3.7 Sonnet LLM" "claude"
copy_llm_python_files "./Gemini 2.0" "gemini"

./runner.sh
