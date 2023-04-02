## Repository for CS213 Final Project
### A Database to sort unique words spoken by the Supreme court.
---
## This is a work in progress (=
---
### Backend:
 - Redis Database as storage.
 - Rust program to insert the data to redis.
 - Python to query the data stored in redis.
---
### Frontend:
 - Redis Stack Web based or application GUI. `http://localhost:8001` or `redis://localhost:6379`
 - (python-webapp branch only) [Work in Proggress] - Return top 10 scores in word_freq sorted set and display in browser.
---
### Reminder:
 - Localhost throws os error (duplicate port binding) make sure to find a way to fetch ipv4 of redis instance.
 - When cloning repo, be sure to double check IP information at `./sort-db-words.py` and `./rusty-redis/srcmain.rs` 
