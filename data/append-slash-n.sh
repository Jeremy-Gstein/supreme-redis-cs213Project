#!/bin/bash
# When converting XML > txt. The Text will be a gigantic string on a single line. 
# The Parser (main.rs) relies on segemting text into redis via counting new lines.

# Use awk for this. Process input and append delimiter.


if [[ $@ -eq 0 ]]; then
	echo "Error."
	echo "Usage: ./append-slash-n.sh file.txt"
	echo "Default segement: 1000 words."
	exit 0;
fi

echo "[+] Parsing Text File $1. Adding Lines.";
awk '{ for (i = 1; i <= NF; i++) { printf "%s%s", $i, (++count % 100 ? " " : "\n") } }' $1 > output.txt;
echo "[+] Completed. $1. New Line Count: $(wc -l output.txt)";
exit 0;
