# This iterative heap is done by me 
class Heap:
    def __init__(self, size):
        self.heap = [None for _ in range(size)]
        
class MaxHeap:
    def __init__(self, size):
        self.maxHeap = Heap(size)
        self.length = size 
        self.count = -1 
        
    def insert(self, element):
        if self.count == -1:
            self.maxHeap.heap[self.count + 1] = element
            self.count += 1
            return self.maxHeap.heap
        self.maxHeap.heap[self.count + 1] = element
        self.count += 1
        return self.siftUp(self.count)
    
    def swap(self, low, high):
        self.maxHeap.heap[high], self.maxHeap.heap[low] = self.maxHeap.heap[low], self.maxHeap.heap[high]
        return 
  
    def siftUp(self, position):
        while True:
            parent = (position - 1) // 2
            if position <= 0 or self.maxHeap.heap[parent] >= self.maxHeap.heap[position]:
                return
            # Swap
            self.swap(parent, position)
            position = parent
        return self.maxHeap.heap

    def siftUp(self, position):
        parent = (position - 1) // 2
        while position and self.maxHeap.heap[position] > self.maxHeap.heap[parent]:
            self.swap(parent, position)
            position = parent
            parent = (position - 1) // 2
        return self.maxHeap.heap
        
    def extract(self):
        if self.count == -1:
            return "Heap is empty"
        self.maxHeap.heap[0] = self.maxHeap.heap[self.count]
        self.maxHeap.heap[self.count] = None
        self.count -= 1
        return self.siftDown(0)
        
    
    def siftDown(self, position):
        while position >= 0:
            left = (2 * position) + 1
            right = (2 * position) + 2
            if left > self.count or right > self.count:
                if left <= self.count and self.maxHeap.heap[left] > self.maxHeap.heap[position]:
                    return self.swap(position, left)
                if right <= self.count and self.maxHeap.heap[right] > self.maxHeap.heap[position]:
                    return self.swap(position, right)
                return
            
            if self.maxHeap.heap[left] > self.maxHeap.heap[right] and self.maxHeap.heap[left] > self.maxHeap.heap[position]:
                self.swap(position, left)
                position = left
        
            elif self.maxHeap.heap[right] > self.maxHeap.heap[left] and self.maxHeap.heap[right] > self.maxHeap.heap[position]:
                self.swap(position, right)
                position = right
            else:
                return 
        return self.maxheap.heap
        
        
    def sort(self):
        while 0 < self.count:
            self.swap(0, self.count)
            self.count -= 1
            self.siftDown(0)
        return self.maxHeap.heap
            

# example from the book page 402 and it is my implementation
            
# heap = MaxHeap(11)
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
# heap.sort()








#----------------------------------------
#This is the same as the above I put it here just in case if im missing anything from the heap DS above
class Heap:
    def __init__(self, size):
        self.heap = [None for _ in range(size)]
        
class MaxHeap:
    def __init__(self, size):
        self.maxHeap = Heap(size)
        self.length = size 
        self.count = -1 
        
    def insert(self, element):
        if self.count == -1:
            self.maxHeap.heap[self.count + 1] = element
            self.count += 1
            return self.maxHeap.heap
        self.maxHeap.heap[self.count + 1] = element
        self.count += 1
        return self.siftUp(self.count)
    
    def swap(self, low, high):
        self.maxHeap.heap[high], self.maxHeap.heap[low] = self.maxHeap.heap[low], self.maxHeap.heap[high]
        return 
  
    def siftUp(self, position):
        while True:
            parent = (position - 1) // 2
            if position <= 0 or self.maxHeap.heap[parent] >= self.maxHeap.heap[position]:
                return
            # Swap
            self.swap(parent, position)
            position = parent
        return self.maxHeap.heap
        
    def extract(self):
        if self.count == -1:
            return "Heap is empty"
        self.maxHeap.heap[0] = self.maxHeap.heap[self.count]
        self.maxHeap.heap[self.count] = None
        self.count -= 1
        return self.siftDown(0)
        
    
    def siftDown(self, position):
        while position >= 0:
            left = (2 * position) + 1
            right = (2 * position) + 2
            if left > self.count or right > self.count:
                if left <= self.count and self.maxHeap.heap[left] > self.maxHeap.heap[position]:
                    return self.swap(position, left)
                if right <= self.count and self.maxHeap.heap[right] > self.maxHeap.heap[position]:
                    return self.swap(position, right)
                return
            
            if self.maxHeap.heap[left] > self.maxHeap.heap[right] and self.maxHeap.heap[left] > self.maxHeap.heap[position]:
                self.swap(position, left)
                position = left
        
            elif self.maxHeap.heap[right] > self.maxHeap.heap[left] and self.maxHeap.heap[right] > self.maxHeap.heap[position]:
                self.swap(position, right)
                position = right
            else:
                return

        return self.maxheap.heap
        
        
    def sort(self):
        while 0 < self.count:
            self.swap(0, self.count)
            self.count -= 1
            self.siftDown(0)
        return self.maxHeap.heap
        
        
    def heapify(self):
        if self.count == -1:
            return False
        n = self.count
        while -1 < n:
            self.siftDown(n)
            n -= 1
        return self.maxHeap.heap
            
            


# if you want to sort in an increasing order, you just create a maxHeap and sort.
# if you want ot sort in decrasing order order, you just create minHeap and sort.
# I discovered this teq in 09/06/202
# heap = MaxHeap(11)
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
# heap.sort()








