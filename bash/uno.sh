#!/bin/bash
DIR=$1
CSV=$2
EXE=$3
OPTS=$4

PARSER=./python/uno-parser.py
echo "File, Line, Error" > $CSV

echo "$DIR\\n$CSV\\n$EXE"

echo "-----------------RUNNING UNO"
set -o xtrace
$EXE $DIR/*.c $OPTS > uno.out
set +o xtrace
echo "=================RUNNING UNO"
OUT=$(pwd)
OUT="$OUT/uno.out"
echo $(python3 $PARSER $OUT >> $CSV)
rm $OUT
