use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use redis::Commands;

const MAX_SET_SIZE: usize = 1000;

fn main() -> redis::RedisResult<()> {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut sets: Vec<Vec<String>> = Vec::new();
    let mut current_set: Vec<String> = Vec::new();
    let mut count = 0;

    for line in reader.lines() {
        let line = line?;

        current_set.push(line);

        if current_set.len() >= MAX_SET_SIZE {
            sets.push(current_set);
            current_set = Vec::new();
            count += 1;
        }
    }

    if !current_set.is_empty() {
        sets.push(current_set);
    }

<<<<<<< HEAD
    let client = redis::Client::open("redis://0.0.0.0/")?;
=======
    let client = redis::Client::open("redis://localhost/")?;
>>>>>>> 9368f3d4a00de5c3aa7b5f5c89f1b42d9ec77899
    let mut conn = client.get_connection()?;

    for (i, set) in sets.iter().enumerate() {
        let key = format!("set_{}", i);
        let _: usize = conn.sadd(&key, &set[..])?;
    }

    Ok(())
}

