DIR=$1
CSV=$2
EXE=$3
OPTS=$4

echo "CALLING SPARSE.SH"
echo "DIR = ${DIR}"
echo "CSV = ${CSV}"
echo "EXE = ${EXE}"
echo "OPTS = ${OPTS}"

PARSER=./python/sparse-parser.py
echo "File, Line, Error" > $CSV

echo "-----------------RUNNING SPARSE"
$EXE $DIR/*.c $OPTS 2> sparse.out
echo "=================RUNNING SPARSE"

OUT=$(pwd)
OUT="$OUT/sparse.out"
echo $(python3 $PARSER $OUT >> $CSV)
rm $OUT
