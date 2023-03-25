#!/bin/bash

# Bash script for repetitive tasks when cloning into this repo.


# untar compressed text-data
get_tar_data () {
	FILE=SCD-1937.txt.tar 
	if [ -f "$FILE" ]; then
		echo "[+] Extracting: $FILE"
		tar xvf $FILE
	fi
}

start_container() {
	echo "[x] Starting Redis DB Container... "
	docker compose up -d
	echo "[+] Redis is up!"
}
# Call Functions here:

get_tar_data
start_container

