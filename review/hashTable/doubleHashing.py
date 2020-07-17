class Table:
    def __init__(self, size):
        self.array = [None] * size 
        self.M = size

    # Original hash function 
    def hash(self, key):
        return key % self.M
    
    # Modified hash function 
    def modifiedHash(self, key, home, i):
        return (home + i) % self.M
     
    # Modified hash function with a constant   
    def constantHash(self, key, home, i):
        c = 3
        return (home + i*c) % self.M


    # quadratic hash function    
    def quadratichash(self, key, home, i):
        return (home + i**2) % self.M
        
    # A second hash function for double hashing
    # The formula is: 1 + key % m' where m' is slightly less then the table size
    def secondHashing(self, key):
        return 1 + key % (self.M - 1)
    
    # Double hashing
    def doubleHashing(self, key, home, i):
        return (home + i * (self.secondHashing(key))) % self.M

    
    # This function searches for a None slot to insert into it or it searches for a given key
    def _search(self, key):
        home = self.hash(key)
        slot = home
        i = 0
        while self.array[slot] != None:
            if self.array[slot] == key:
                return slot
            i += 1
            slot = self.doubleHashing(key, home, i)
        if self.array[slot] == None:
            return slot
        return "Table is full"
        
    
    def insert(self, key):
        slot = self._search(key)
        if self.array[slot] == None:
            self.array[slot] = key
            return self.array
        return slot
        
    
    def searchKey(self, key):
        slot = self._search(key)
        if self.array[slot] == key:
            return slot
        return "Not found"
        
    def delete(self, key):
        slot = self._search(key)
        if self.array[slot] == key:
           self.array[slot] = "∆"
           return self.array
        return "Not found"
            
    
            
            

# table = Table(13)
# table.insert(765)
# table.insert(431)
# table.insert(96)
# table.insert(142)
# table.insert(579)
# table.insert(226)
# table.insert(903)
# table.insert(388)

