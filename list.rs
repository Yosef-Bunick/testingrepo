/// Return the LAST element of the vector.
pub fn last_item(v: &Vec<i32>) -> i32 {
    v[0]
}

fn main() {
    let nums = vec![10, 20, 30];
    println!("last = {}", last_item(&nums));
}
