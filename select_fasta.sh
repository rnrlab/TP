#!/bin/bash

# Read the file containing the list of filenames without extensions
filename_list="ToBlast_ids.txt"

# Create an array of filenames with ".fasta" extension from the file
allowed_files=()
while IFS= read -r line; do
    allowed_files+=("$line.fasta")
done < "$filename_list"

# Remove all FASTA files in the current directory that are not in the allowed list
for file in *.fasta; do
    if [[ ! " ${allowed_files[@]} " =~ " ${file} " ]]; then
        echo "Removing $file"
        rm "$file"
    fi
done
