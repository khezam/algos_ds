class Table:
    def __init__(self, size):
        self.array = [None] * size 
        self.M = size
        self.n = 0
        
    def hash(self, key):
        return key % self.M
        
    def modifiedHash(self, key, home, i):
        return (home + i) % self.M
        
    def constantHash(self, key, home, i):
        c = 3
        return (home + i*c) % self.M
        
    def quadratichash(self, key, home, i):
        return (home + i**2) % self.M
    
    # The P =  (self.M - 1) where P is a number the slightly less than the size of Table
    # Pg 273 by cohen book
    def secondHashing(self, key):
        return 1 + key % (self.M - 1)
        
    def doubleHashing(self, key, home, i):
        return (home + i * (self.secondHashing(key))) % self.M
    
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
        
    def rehash(self):
        OriginalTable = self.array
        originalArraySize = self.M
        self.M = ((self.M * 2) + 1) 
        self.array = [None] * self.M
        self.n = 0
        i = 0
        while i < originalArraySize:
            if OriginalTable[i] != None:
                self.insert(OriginalTable[i])
            i += 1
        return self.array
        
    def insert(self, key):
        # When LoadFactor is greater the half of the table size, then start rehashing
        loadFactor = self.n / self.M
        if loadFactor <= 0.5:
            slot = self._search(key)
            if self.array[slot] == None:
                self.array[slot] = key
                self.n += 1
                return self.array
            return slot
        self.rehash()
        return self.insert(key)
        
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



