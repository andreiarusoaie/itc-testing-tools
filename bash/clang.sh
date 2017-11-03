DIR=$1
CSV=$2
EXE=$3
OPTS=$4

echo "$DIR\n$CSV\n$EXE\n$OPTS\n"

PARSER=../python/clang-parser.py
echo "File, Line, Error" > $CSV

echo "$EXE $OPTS $DIR/*.c $DIR/*.cpp  2> clang-output.txt"
OUT=$(pwd)
OUT="$OUT/clang-output.txt"
echo $(python3 $PARSER $OUT >> $CSV)
rm -f $OUT


