DIR=$1
CSV=$2

rm $CSV
echo "File,Line,CWE, Defect Type, Defect Sub-Type" >> $CSV

echo "Gathering errors..."
echo "Working dir: $DIR"

FILES=$(ls $DIR | egrep '\.c$|\.cpp$')
for f in $FILES
do
    # current file
    C_FILE=$DIR$f

    # reset 
    CWE="unknown"
    D="unknown"
    DS="unknown"

    # collect CWE, Defect Type, Defect Sub-type
    CWE=$(grep "CWE" $C_FILE | cut -d ":" -f 2)
    D=$(grep "Defect Type" $C_FILE -m 1 | head -1 | cut -d ":" -f 2)
    DS=$(grep "Defect Sub" $C_FILE -m 1 | head -1 | cut -d ":" -f 2)
    
    # collect line number and generate a table row
    grep "Tool should detect this line as error" $C_FILE -n | while read line ; do
	LN=$(echo $line | cut -d ':' -f 1)
	echo "$f, $LN, $CWE, $D, $DS" >> $CSV
    done
    
done

echo "Done.\nOutput written in $CSV.\n"
