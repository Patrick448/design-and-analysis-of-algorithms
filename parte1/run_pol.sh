#!/bin/bash

# Name of the compiled C++ binary
EXEC="./polynomial"

# Modes to test
MODES=("iter" "rec" "ai_iter" "ai_rec")

# Repeat count
REPEAT=100

# Output file
OUTPUT="pol_results.csv"
echo "mode,n,time_ns,result" > $OUTPUT

# Loop through each mode and n
for mode in "${MODES[@]}"; do
    for n in $(seq 1 20 1000); do
        for run in $(seq 1 $REPEAT); do
            result=$($EXEC $mode $n 1)
            echo "$result" >> $OUTPUT
            echo "ran $mode $n"
        done
    done
done
