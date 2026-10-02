#!/bin/bash
# count_seq.sh - Count the number of sequences in a FASTA file

file=$1
n=$(grep -c ">" "$file")
echo "$file contains $n sequences"