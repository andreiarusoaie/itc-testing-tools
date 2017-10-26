DIR=$1
CSV=$2

rm $CSV
echo "File,Count" >> $CSV


echo "Working dir: $DIR"
echo
FILES=$(ls $DIR | egrep '\.c$|\.cpp$')
for f in $FILES
do
    C_FILE=$DIR$f
    # echo $C_FILE
    # cat $C_FILE
    R=$(grep "Tool should detect this line as error" $C_FILE | wc -l)
    echo "$f,$R" >> $CSV
done
