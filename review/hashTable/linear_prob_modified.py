class Table:
    def __init__(self, size):
        self.array = [None] * size 
        self.M = size 
        
    def hash(self, key):
        return key % self.M
        
    def modifiedHash(self, key, home, i):
        return (home + i) % self.M
    
    def _search(self, key):
        home = self.hash(key)
        slot = home
        i = 0
        while self.array[slot] != None and slot+1 != home:
            if self.array[slot] == key:
                return slot
            i += 1
            slot = self.modifiedHash(key, home, i)
        if self.array[slot] == None:
            return slot
        return "Table is full"
        
    
    def insert(self, key):
        slot = self._search(key)
        if isinstance(slot, str):
            return slot
        self.array[slot] = key
        return self.array
        
    
    def searchKey(self, key):
        slot = self._search(key)
        if isinstance(slot, str):
            return "Not found"
        return slot
        
    def delete(self, key):
        slot = self._search(key)
        if isinstance(slot, str):
            return "Not found"
        self.array[slot] = "∆"
        return self.array
            
    
            
            

# table = Table(13)
# table.insert(765)
# table.insert(431)
# table.insert(96)
# table.insert(142)
# table.insert(579)
# table.insert(226)
# table.insert(903)
# table.insert(388)


