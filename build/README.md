## NOTE: repo IPv4 is set to '10.0.0.22' (my test machine)
##       This needs to be changed to 'localhost' for portability.
## 1.  Make sure Redis DB is already running.
### in ./build run the 'run-app.sh' script.
## `./run-app.sh`

## 2.  Run `docker compose up -d` 

## if cache issued. remove hanging images with:
	`docker compose build cs213-project-jg --no-cache`

# CMD for Redis container:
	`docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest`
