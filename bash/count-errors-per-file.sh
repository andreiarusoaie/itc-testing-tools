DIR_W=$1
DIR_WO=$2
CSV=$3

rm -f $CSV
echo "File,Count W, Count W/o" >> $CSV

echo "Counting errors..."
echo "Working dir: $DIR"

FILES=$(ls $DIR_W | egrep '\.c$|\.cpp$')
for f in $FILES
do
    W=$(grep "Tool should detect this line as error" $DIR_W$f | wc -l)
    WO=$(grep "Tool should not detect this line as error" $DIR_WO$f | wc -l)
    echo "$f,$W,$WO" >> $CSV
done

echo "Done.\nOutput written in $CSV.\n"
