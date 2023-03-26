## Make sure Redis DB is already running.

## Run `docker compose up -d` 

## if cache problems persist. remove hanging images with:
	`docker rmi archlinux:latest`

# CMD for Redis container:
	`docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest`
