DIR=$1
CSV=$2
EXE=$3
OPTS=$4

echo "$DIR\n$CSV\n$EXE\n$OPTS"

PARSER=./python/clang-parser.py
echo "File, Line, Error" > $CSV

OUT=$(pwd)
OUT="$OUT/clang-output.txt"
echo $($EXE $OPTS $DIR/*.c 2> $OUT)
echo $(python3 $PARSER $OUT >> $CSV)
rm -f $OUT
