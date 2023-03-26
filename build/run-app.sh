#!/bin/bash

check_container_health() {
	# Check if the container is healthy
	if curl -I localhost:8001 2>&1 | grep -q "Connection refused"; then
  		echo "Container is not healthy" 
		check_container_health
	else
  		echo "Container is healthy"
	fi
}

start_app() {
	echo "[x] Starting Redis DB Instance on port 6379."	
	$(tail -n 1 ./README.md | bash)
	echo "[+] Redis is Stating.. $(docker ps)"
		
	check_container_health	
	
}

#MAIN
start_app
