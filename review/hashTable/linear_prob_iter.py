class Table:
    def __init__(self, size):
        self.array = [None] * size
        self.n = size
        
        
    def hash(self, key):
        return key % self.n
        
    
    def _search(self, key, slot):
        new_slot = slot + 1
        while self.array[new_slot] != None and new_slot != slot:
            if self.array[new_slot] == key:
                return new_slot
            if new_slot == self.n - 1:
                new_slot = -1
            new_slot += 1
        if self.array[new_slot] == None:
            return new_slot
        return "Table is full"
    
    def insert(self, key):
        slot = self.hash(key)
        if self.array[slot] == None:
            self.array[slot] = key
            return self.array
        slot = self._search(key, slot)
        self.array[slot] = key
        return self.array
        
    def searchKey(self, key):
        slot = self.hash(key)
        if self.array[slot] == key:
            return slot
        slot = self._search(key, slot)
        if self.array[slot] == key:
            return slot
        return "Not found"
        
    def delete(self, key):
        slot = self.searchKey(key)
        if self.array[slot] == key:
            self.array[slot] = '∆'
            return self.array
        return slot
    
            
            

# table = Table(13)
# table.insert(765)
# table.insert(431)
# table.insert(96)
# table.insert(579)
# table.insert(142)
# table.insert(226)
# table.insert(903)
# table.insert(388)
# table.delete(226)
# table.searchKey(903)

