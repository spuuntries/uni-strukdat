from hashtable import HashTable


def test_hashtable(collision_resolution):
    print(f"Testing HashTable with {collision_resolution} collision resolution:")

    ht = HashTable(collision_resolution=collision_resolution)

    # Test putting key-value pairs
    ht.put("apple", 5)
    ht.put("banana", 10)
    ht.put("orange", 7)

    # Test getting values by key
    print("Value for 'apple':", ht.get("apple"))
    print("Value for 'banana':", ht.get("banana"))
    print("Value for 'orange':", ht.get("orange"))

    # Test updating a value
    ht.put("apple", 8)
    print("Updated value for 'apple':", ht.get("apple"))

    # Test getting a non-existent key
    print("Value for 'grape':", ht.get("grape"))

    # Test __setitem__ and __getitem__ methods
    ht["pear"] = 12
    print("Value for 'pear':", ht["pear"])

    # Test collision resolution
    ht.put("papaya", 6)
    ht.put("mango", 9)
    print("Value for 'papaya':", ht.get("papaya"))
    print("Value for 'mango':", ht.get("mango"))

    # Test growing the hash table
    for i in range(256):
        ht.put(f"key{i}", i)
    print("Size of the hash table after growth:", ht.size)

    print()


# Test separate chaining collision resolution
test_hashtable("separate_chaining")

# Test linear probing collision resolution
test_hashtable("linear")

# Test quadratic probing collision resolution
test_hashtable("quadratic")

# Test double hashing collision resolution
test_hashtable("double_hashing")
