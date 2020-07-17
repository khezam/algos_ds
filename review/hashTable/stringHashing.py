"""
For a string, say `abcde`, a very effective function is treating this as number of prime number base `p`. 
Let's elaborate this statement. 

For a number, say `578`, we can represent this number in base 10 number system as 5*10^2 + 7*10^1 + 8*10^0$$

Similarly, we can treat `abcde` as a * p^4 + b * p^3 + c * p^2 + d * p^1 + e * p^0

Here, we replace each character with its corresponding ASCII value. 

A lot of research goes into figuring out good hash functions and this hash function is one of the most popular functions used for strings. 
We use prime numbers because the provide a good distribution. The most common prime numbers used for this function are 31 and 37.
"""

"""Thus, using this algorithm, we can get a corresponding integer value for each string key and store it in the array.

Note that the array used for this purpose is called a `bucket array`. 
It is not a special array. We simply choose to give a special name to arrays for this purpose. 
Each entry in this `bucket array` is called a `bucket` and the index in which we store a bucket is called `bucket index`.

Let's add these details to our class.
"""


class HashMap:
    
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37
        self.num_entries = 0
        
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
    
    def get_bucket_index(self, key):
        return self.get_hash_code(key)
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.p
            current_coefficient = current_coefficient

        return hash_code


# hash_map = HashMap()

# bucket_index = hash_map.get_bucket_index("abcd")
# print(bucket_index)


# hash_map = HashMap()

# bucket_index = hash_map.get_bucket_index("bcda")
# print(bucket_index)









"""Compression Function

We now have a good hash function which will return unique values for unique objects. But let's look at the values. These are huge. We cannot create such large arrays. So we use another function - `compression function` to compress these values so as to create arrays of reasonable sizes. 

A very simple, good, and effective compression function can be ` mod len(array)`. The `modulo operator %` returns the remainder of one number when divided by other. 

So, if we have an array of size 10, we can be sure that modulo of any number with 10 will be less than 10, allowing it to fit into our bucket array.

Because of how modulo operator works, instead of creating a new function, we can write the logic for compression function in our `get_hash_code()` function itself.
"""
class HashMap:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(keu)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient

        return hash_code % num_buckets                                # one last compression before returning
    
    
    def size(self):
        return self.num_entries

"""
Collision Handling

As discussed earlier, when two different inputs produce the same output, then we have a collision. Our implementation of `get_hash_code()` function is satisfactory. 
However, because we are using compression function, we are prone to collisions. 

Consider the following scenario. 

We have a bucket array of length 10 and we get two different hash codes for two different inputs, say 355, and 1095. 
Even though the hash codes are different in this case, the bucket index will be same because of the way we have implemented our compression function. 
Such scenarios where multiple entries want to go to the same bucket are very common. So, we introduce some logic to handle collisions.

There are two popular ways in which we handle collisions.

1. Closed Addressing or Separate chaining
2. Open Addressing

1. Closed addressing is a clever technique where we use the same bucket to store multiple objects. The bucket in this case will store a linked list of key-value pairs. Every bucket has it's own separate chain of linked list nodes.

2. In open addressing, we do the following:
    * If, after getting the bucket index,  the bucket is empty, we store the object in that particular bucket
    
    * If the bucket is not empty, we find an alternate bucket index by using another function which modifies the current hash code to give a new code
    

Separate chaining is a simple and effective technique to handle collisions and that is what we discuss here. 

Implement the `put` and `get` function using the idea of separate chaining. 
"""

# Done by Udacity
class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient

        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        return self.num_entries



# Done by me(the get() function and put() function)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        slot = self.get_bucket_index(key)
        new_node = Node(key, value)
        if self.bucket_array[slot] == None:
            self.bucket_array[slot] = new_node
        else:
            node = self.bucket_array[slot]
            while node.next:
                node = node.next
            node.next = new_node
        self.num_entries += 1
        return self.bucket_array
            
        
    
    def get(self, key):
        slot = slot = self.get_bucket_index(key)
        if self.bucket_array[slot] == None:
            return
        node = self.bucket_array[slot]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return False
        
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                      
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   

        return hash_code % num_buckets                               
    
    
    def size(self):
        return self.num_entries

hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("neo", 11)
hash_map.put("two", 2)
hash_map.put("three", 3)


print("size: {}".format(hash_map.size()))
print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))










