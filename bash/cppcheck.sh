DIR=$1
CSV=$2
EXE=$3
OPTS=$4

echo "CALLING CPPCHECK.SH"
echo "DIR = ${DIR}"
echo "CSV = ${CSV}"
echo "EXE = ${EXE}"
echo "OPTS = ${OPTS}"

PARSER=./python/cppcheck-parser.py
echo "File, Line, Error" > $CSV

echo "$DIR\n$CSV\n$EXE\n$OPTS"

echo "HERE HERE-------------"
set -o xtrace
$EXE --quiet $DIR $OPTS 2> cppcheck-output.xml
set +o xtrace
echo "HERE HERE============="

XML=$(pwd)
XML="$XML/cppcheck-output.xml"
python3 $PARSER $XML >> $CSV
rm $XML
