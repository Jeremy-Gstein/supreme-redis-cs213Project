use redis::Commands;

fn main() -> redis::RedisResult<()> {
    let dest_key = "union_key";
    let set_keys: Vec<String> = (1..=851).map(|i| format!("set_{}", i)).collect();

    let client = redis::Client::open("redis://10.0.0.40/")?;
    let con = client.get_connection()?;

    // Add items to each set
    for (i, key) in set_keys.iter().enumerate() {
        let set_items: Vec<&str> = vec!["item1", "item2", "item3"];
        let _: () = con.sadd_multiple(key, &set_items)?;
    }

    // Compute the union of all sets and store the result in dest_key
    let _: usize = con.sunionstore(dest_key, &set_keys.iter().map(|s| s.as_str()).collect::<Vec<&str>>())?;

    Ok(())
}

