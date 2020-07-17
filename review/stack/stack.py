class Array:
    def __init__(self, size):
        self.stack = [ None for _ in range(size)]

        

class Stack:
    def __init__(self, size):
        self.stack = Array(size).stack
        self.top = -1
    
    def is_empty(self):
        return self.top == -1

    def push(self, element):
        self.stack[self.top+1] = element
        self.top += 1
        return self.stack
        
    def peek(self):
        if self.is_empty:
            return "Stack is empty"
        return self.stack[self.top]
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        tmp = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return tmp
    
    def len(self):
        return self.top + 1

    def push(self, data):
        # TODO: Add a conditional to check for full capacity
        loadfactor = self.num_elements
        if loadfactor == self.M :
            self._handle_stack_capacity_full()
        self.arr[self.next_index+1] = data
        self.next_index += 1
        self.num_elements += 1
        
    # TODO: Add the _handle_stack_capacity_full method
    def _handle_stack_capacity_full(self):
        originalArr = self.arr
        originalSize = self.M
        self.M = (originalSize * 2)
        self.next_index = -1
        self.num_elements = 0
        self.arr = [ 0 for _ in range(self.M)]
        i = 0 
        while i < originalSize:
            if originalArr[i] != None:
                self.push(originalArr[i])
            i += 1
        return self.arr
        
        
    def isValidSource(self, line):
        for token in line: 
            if token in "{[(" :
                self.push(token) 
            elif token in "}])" :
                if self.is_empty() : 
                    return False
                else :
                    left = self.pop()
                    if (token == "}" and left != "{") or (token == "]" and left != "[") or (token == ")" and left != "(") : 
                        return False
        return self.is_empty()
        

stack = Stack(20)
stack.isValidSource('{A + (B * C) - (D / [E + F])}')

        