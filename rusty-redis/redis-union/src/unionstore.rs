use redis::{Client, Commands};

const NUM_SETS: usize = 851;
const MAX_SET_SIZE: usize = 1000;

fn main() -> redis::RedisResult<()> {
    let client = Client::open("redis://10.0.0.40/")?;
    let mut conn = client.get_connection()?;

    // Generate the set keys and add items to the sets
    for i in 1..=NUM_SETS {
        let key = format!("set_{}", i);
        let set_size = MAX_SET_SIZE.min(i * 10); // adjust set size for testing purposes
        let set_items: Vec<String> = (1..=set_size).map(|j| format!("item_{}_{}", i, j)).collect();
        let _: () = conn.sadd_multiple(&key, &set_items)?;
    }

    // Merge the sets into a union store
    let set_keys: Vec<String> = (1..=NUM_SETS).map(|i| format!("set_{}", i)).collect();
    let dest_key = "union";
    let _: usize = conn.sunionstore(dest_key, &set_keys)?;

    Ok(())
}

