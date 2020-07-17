class Heap:
    def __init__(self, size):
        self.heap = [None] * size 
        self.length = size 
        self.count = -1 
    
    
    def insert(self, element):
        if self.count == -1:
            self.heap[self.count + 1] = element
            self.count += 1
            return self.heap
        self.heap[self.count + 1] = element
        self.count += 1
        return self.siftUp(self.count)
        
    def swap(self, first, last):
        tmp = self.heap[last]
        self.heap[last] = self.heap[first]
        self.heap[first] = tmp
        return 
    
    def siftUp(self, position):
        parent = (position - 1) // 2
        if position <= 0 or self.heap[position] <= self.heap[parent]:
            return self.heap
        self.swap(parent, position)
        return self.siftUp(parent)
        
        
    def extract(self):
        if self.count == -1:
            return "Heap is empty"
        self.heap[self.count - self.count] = self.heap[self.count]
        self.heap[self.count] = None
        self.count -= 1
        return self.siftDown(self.count - self.count)
    
    def siftDown(self, position):
        left = (2 * position) + 1
        right = (2 * position) + 2
        if left > self.count or right > self.count:
            if left <= self.count and self.heap[left] > self.heap[position]:
                return self.swap(position, left)
            if right <= self.count and self.heap[right] > self.heap[position]:
                return self.swap(position, right)
            return 
        if self.heap[left] > self.heap[right] and self.heap[position] < self.heap[left]:
            self.swap(position, left)
            return self.siftDown(left)
        if self.heap[right] > self.heap[left] and self.heap[position] < self.heap[right]:
            self.swap(position, right)
            return self.siftDown(right)
        return self.heap
        
    # this function to use heapify from a given complete binary tree and we want make it maxHeap
    # watch abdul bari video
    def _siftDown(self, position):
        left = (2 * position) + 1
        right = (2 * position) + 2
        if left > self.count or right > self.count:
            if left <= self.count and self.heap[left] < self.heap[position]:
                return self.swap(position, left)
            if right <= self.count and self.heap[right] < self.heap[position]:
                return self.swap(position, right)
            return 
        if self.heap[left] < self.heap[right] and self.heap[position] > self.heap[left]:
            self.swap(position, left)
            return self._siftDown(left)
        if self.heap[right] < self.heap[left] and self.heap[position] > self.heap[right]:
            self.swap(position, right)
            return self._siftDown(right)
        return self.heap



    # pg 403 to see an example od using a heap to sort
    def _siftDown(self, position):
        left = (2 * position) + 1
        right = (2 * position) + 2
        if left > self.count or right > self.count:
            if left <= self.count and self.heap[left] > self.heap[position]:
                return self.swap(position, left)
            if right <= self.count and self.heap[right] > self.heap[position]:
                return self.swap(position, right)
            return 
        if self.heap[left] > self.heap[right] and self.heap[position] < self.heap[left]:
            self.swap(position, left)
            return self._siftDown(left)
        if self.heap[right] > self.heap[left] and self.heap[position] < self.heap[right]:
            self.swap(position, right)
            return self._siftDown(right)
        return self.heap
        
    
    def sort(self):
        while 0 < self.count:
            self.swap(0, self.count)
            self.count -= 1
            self._siftDown(0)
        return self.heap
    
    def heapify(self):
        if self.count == -1:
            return False
        n = self.count
        while -1 < n:
            self._siftDown(n)
            n -= 1
        return self.heap
        


# heap = Heap(11)
# heap.insert(10)
# heap.insert(51)
# heap.insert(2)
# heap.insert(18)
# heap.insert(4)
# heap.insert(31)
# heap.insert(13)
# heap.insert(5)
# heap.insert(23)
# heap.insert(64)
# heap.insert(29)
# heap.heapify()






