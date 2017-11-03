DIR=$1
CSV=$2
EXE=$3
OPTS=$4

echo "$DIR\n$CSV\n$EXE\n$OPTS"

PARSER=../python/infer-parser.py
echo "File, Line, Error" > $CSV

echo $(cd $DIR ; make clean ; $EXE run -- make > /dev/null ; cd -)
echo $(python3 $PARSER $DIR/infer-out/report.json > $CSV)
