DIR=$1
CSV=$2
EXE=$3
OPTS=$4

PARSER=../python/cppcheck-parser.py
echo "File, Line, Error" > $CSV

echo "$DIR\n$CSV\n$EXE\n$OPTS"

echo $($EXE --quiet $DIR $OPTS 2> cppcheck-output.xml)
XML=$(pwd)
XML="$XML/cppcheck-output.xml"
echo $(python3 $PARSER $XML >> $CSV)
rm $XML
