## Repository for CS213 Final Project
#### A Database to sort unique words spoken by the United States Supreme Court.
#### All Data was sourced from https://www.govinfo.gov/help/scd
####  Data contains all US Supreme Court Decisions between 1937 and 1975.
![image](https://user-images.githubusercontent.com/66806528/235373556-2abc0584-2e53-42d2-a25c-9dee87ae1405.png)
---
#### This is a work in progress (=
---
### Backend:
 - Redis Database as storage.
 - Rust program to insert the data to redis.
 - Python to query the data stored in redis.
---
### Frontend:
 - Redis Stack Web based or application GUI. `http://localhost:8001` or `redis://localhost:6379`
 - a Flask application to search the redis DB for scores.
 ![image](https://github.com/Jeremy-Gstein/supreme-redis-cs213Project/assets/66806528/3b8a6705-bb26-4a48-844d-a6e582317ae8)
---
### Research Paper:
 - todo (^:
---
### Reminder:
 - When cloning repo, be sure to double check IP information at `./sort-db-words.py` and `./rusty-redis/src/main.rs` 
