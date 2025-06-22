#!/bin/bash

# Name of the compiled C++ binary
EXEC="./fibonacci"

# Modes to test
MODES=("iter" "rec" "ai_iter" "ai_rec")

# Repeat count
REPEAT=100

# Output file
OUTPUT="fib_results.csv"
echo "mode,n,time_ns,result" > $OUTPUT

# Loop through each mode and n
for mode in "${MODES[@]}"; do
    for n in {1..20}; do
        for run in $(seq 1 $REPEAT); do
            result=$($EXEC $mode $n)
            echo "$result" >> $OUTPUT
        done
    done
done
