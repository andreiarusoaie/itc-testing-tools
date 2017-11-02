CSV_ERROR=$1
CSV_WO_ERROR=$2
OUT_CSV=$3

rm -f $OUT_CSV
echo "Merging $CSV_ERROR $CSV_WO_ERROR into $OUT_CSV"
paste $CSV_ERROR $CSV_WO_ERROR | while read line ; do
    FILE=$(echo $line | cut -d ',' -f 1)
    LN1=$(echo $line | cut -d ',' -f 2)
    LN2=$(echo $line | cut -d ',' -f 6)
    DEFECT_TYPE=$(echo $line | cut -d ',' -f 8)
    DEFECT_SUBTYPE=$(echo $line | cut -d ',' -f 9)
    echo "$FILE, $LN1, $LN2, $DEFECT_TYPE, $DEFECT_SUBTYPE" >> $OUT_CSV
done
echo "Done merging."
