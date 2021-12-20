# Hash Table:   
    # is a data structure that stores data in key:value pairs in an efficient way
    # it uses a hash function to compute an index position of an array/list in which an element will be stored
    # the data is stored in slots which are also called buckets
    # Lookup, Insert & Delete operations can be done in contstant O(1) time.
    # Python dictionaries are an example of a hash table

# Hash Function:
    # An algorithm that converts a hash key to a hash value
    # Must always produce the same hash value for the same key
    # Provide a uniform distribution of has values
    # Minimize clustering and be very fast to compute


# Example
class HashItem:                                     # Stores data
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
class HashTable:
    def __init__(self):
        self.size = 256                             # initial size is 256 elements
        self.slots = [None] * self.size             # initialize 256 slots with at value of none to start with
        self.count = 0

    def hashfunction(self, key):
        keystr = str(key)
        hashVal = 0
        for ch in keystr:                           # for each character in our string
            hashVal += ord(ch)                      # hashvalue will increment in value by the ord of ch(character)

        return (hashVal % self.size)                # Modulo Operator 

    def rehashfunction(self, key):                  # Rehashing to calculate a different slot
        keystr = str(key)
        hashVal = 0
        counter = 0
        for ch in str(keystr):
            counter += 1
            hashVal += ord(ch)+counter

        return (hashVal*len(keystr)) % self.size

ht = HashTable()
print(ht.hashfunction('Vanessa Caraballo'))
print(ht.hashfunction('Bob Smith'))
print(ht.hashfunction('Lucifer Taylor'))
print(ht.hashfunction('Jane Doe'))
print(ht.hashfunction('Alex Whites'))
print(ht.hashfunction('Barry Bunny'))
print(ht.hashfunction(4567))
print(ht.hashfunction(7654))
print(ht.rehashfunction(7654))               

# Collisions - Crash and Burn

# A 'Perfect' hash function is one where every key maps to a unique slot after hashing
# Collisions happen when two different keys 'hash' to the same value
# Collision Resolution
    # Open Addressing - Start at the original hash value position and move down the hash table until an open slot is found
    # Rehashing - Use a second hashing function to calculate a different slot to use
    # Chaining - The slots in the hash table are initialized as an empty data structure like a list or binary search tree.
    # Each value is stored in the hash table at its slot position and the value is inserted into the data structure.