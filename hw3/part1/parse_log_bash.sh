#!/bin/bash

FILE=$1;
FILE_TO_SAVE="bash_results.txt";
if [ ! -f "$FILE" ]; then
    echo "$FILE" not a file 1>&2;
    exit 1;
fi

if [ -f "$FILE_TO_SAVE" ] ; then
	rm -f "$FILE_TO_SAVE";
fi
touch "$FILE_TO_SAVE";

echo "---------------- TOTAL REQUESTS NUMBER -------------------" >> "$FILE_TO_SAVE";
grep -c ^ "$FILE" >> "$FILE_TO_SAVE";

echo "" >> "$FILE_TO_SAVE";
echo "---------------- REQUESTS NUMBER BY TYPE -----------------" >> "$FILE_TO_SAVE";
for var in "GET" "POST" "PUT" "HEAD" "DELETE" "OPTIONS" "CONNECT" 
do
	printf "$var: " >>  "$FILE_TO_SAVE";
	grep "$var" "$FILE" | wc -l >>  "$FILE_TO_SAVE";
done

 
echo "" >> "$FILE_TO_SAVE";
echo "---------------- TOP 10 REQUESTS SIZE  -----------------" >> "$FILE_TO_SAVE";
sort -k 10 -rn "$FILE" | awk '{print $10 " :: " $7 " :: " $9}' |  uniq -c |  head -n 10 >>  "$FILE_TO_SAVE";

echo "" >> "$FILE_TO_SAVE";
echo "---------------- TOP 10 CLIENT ERROR WITH IP ------------" >> "$FILE_TO_SAVE";
awk '$9 ~ /4[0-9][0-9]/ {print $7 " :: " $9 " :: " $1}' "$FILE" | sort   | uniq -c | sort -rn | head -n 10 >> "$FILE_TO_SAVE";

echo "" >> "$FILE_TO_SAVE";
echo "---------------- TOP 10 CLIENT ERROR BY SIZE WITH IP ------------" >> "$FILE_TO_SAVE";
awk '$9 ~ /4[0-9][0-9]/ {print $10 " :: " $7 " :: " $9 " :: " $1}' "$FILE" |  sort -rn | uniq -c | head -n 10 >> "$FILE_TO_SAVE";

