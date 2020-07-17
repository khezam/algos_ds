class Heap:
    def __init__(self, size):
        self.array = [None] * size 
        self.count = -1 
        self.size = size 
        
    def insert(self, element):
        if self.count == -1:
            self.array[self.count + 1] = element
            self.count += 1
            return self.array
        self.array[self.count + 1] = element
        self.count += 1
        return self.siftUp(self.count)
        
    def swap(self, left, right):
        tmp = self.array[right]
        self.array[right] = self.array[left]
        self.array[left] = tmp
        return
        
    def siftUp(self, count):
        parent = (count - 1) // 2
        if count <= 0 or self.array[count] <= self.array[parent]:
            return
        self.swap(parent, count)
        return self.siftUp(parent)
        
    def delete(self):
        if self.count == -1:
            return "Heap is empty"
        self.array[self.count - self.count] = self.array[self.count]
        self.array[self.count] = None
        self.count -= 1
        return self.siftDown(self.count - self.count)
        
    def siftDown(self, count):
        left = (2 * count) + 1
        right = (2 * count) + 2
        if self.array[left] == None or self.array[right] == None:
            if self.array[left] != None and self.array[count] < self.array[left]:
                return self.swap(count, left)
            if self.array[right] != None and self.array[count] < self.array[right]:
                return self.swap(count, right)
            return
        if self.array[left] > self.array[right] and self.array[left] > self.array[count]:
            self.swap(count, left)
            return self.siftDown(left)
        if self.array[right] > self.array[left] and self.array[right] > self.array[count]:
            self.swap(count, right)
            return self.siftDown(right)
    
    def sortSiftDown(self, count):
        # Example in pg 402
        left = (2 * count) + 1
        right= (2 * count) + 2
        if left > self.count or right > self.count:
            if left <= self.count and self.array[count] < self.array[left]:
                return self.swap(count, left)
            if right <= self.count and self.array[count] < self.array[right]:
                return self.swap(count, right)
            return 
        if self.array[left] > self.array[right] and self.array[left] > self.array[count]:
            self.swap(count, left)
            return self.sortSiftDown(left)
        if self.array[right] > self.array[left] and self.array[right] > self.array[count]:
            self.swap(count, right)
            return self.sortSiftDown(right)
            
    def sort(self):
        n = self.count
        while 0 < n:
            self.swap(self.count - self.count, n)
            self.count -= 1
            self.sortSiftDown(self.count - self.count)
            n -= 1
        return self.array

    def heapifySiftDown(self, count):
        left = (2 * count) + 1
        right= (2 * count) + 2
        if left > self.size or right > self.size:
            if left <= self.size-1 and self.array[count] < self.array[left]:
                return self.swap(count, left)
            if right <= self.size-1 and self.array[count] < self.array[right]:
                return self.swap(count, left)
            return
        if self.array[left] > self.array[right] and self.array[left] > self.array[count]:
            self.swap(count, left)
            return self.heapifySiftDown(left)
        if self.array[right] > self.array[left] and self.array[right] > self.array[count]:
            self.swap(count, right)
            return self.heapifySiftDown(right)

    def heapify(self, element, size):
        if self.count == -1:
            self.array[size] = element
            self.count += 1
            return self.heapifySiftDown(size)
        self.array[size] = element
        return self.heapifySiftDown(size)
        
            
heap = Heap(7)
items = [5, 10, 30, 20, 35, 45, 15]
n = len(items) - 1

while n >= 0:
    heap.heapify(items[n], n)
    n -= 1
    
