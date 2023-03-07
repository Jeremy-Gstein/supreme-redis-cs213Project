#!/bin/bash

# Bash script for repetitive tasks when cloning into this repo.


# untar compressed text-data
get_tar_data () {
	FILE=SCD-1937.txt.tar 
	if [ -f "$FILE" ]; then
		echo "[+] Extracting: $FILE"
		tar xzvf $FILE
	fi
}


# Call Functions here:

get_tar_data

