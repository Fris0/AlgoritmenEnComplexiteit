#!/bin/bash

# Which input file to check (standard is small.input)
if [ $# -eq 0 ]
then
    FILENAME="small"
else
    FILENAME=$1
fi

# Check if input files exist
if ! [[ -f "$FILENAME.input" && -f "$FILENAME.output" && -f "ex2.py" ]]
then
    echo "PROGRAM NOT ACCEPTED: one or more files not found."
    echo "Make sure $FILENAME.input, $FILENAME.output and ex2.py all exist"
    exit
fi

timeout 10s python ex2.py < "$FILENAME.input" > "$FILENAME.temp.output"
RESULT=$?
if [ $RESULT -eq 0 ]; then

    # Check if output differs from expected output
    if ! diff --strip-trailing-cr "$FILENAME.temp.output" "$FILENAME.output" >/dev/null 2>&1
    then
        echo "PROGRAM NOT ACCEPTED: output differs "
        diff "$FILENAME.temp.output" "$FILENAME.output"
    else
        echo "PROGRAM ACCEPTED"
    fi
else
    echo "PROGRAM NOT ACCEPTED: code exited with error"
fi
if [ $RESULT -eq 124 ]; then
    echo "Execution took too long"
fi
rm "$FILENAME.temp.output"
