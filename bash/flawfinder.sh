DIR=$1
CSV=$2
EXE=$3
OPTS=$4

PARSER=../python/flawfinder-parser.py
echo "File, Line, Error" > $CSV

echo "$DIR\n$CSV\n$EXE\n$OPTS\n"

echo $($EXE $DIR $OPTS > flawfinder.out)
OUT=$(pwd)
OUT="$OUT/flawfinder.out"
echo $(python3 $PARSER $OUT >> $CSV)
