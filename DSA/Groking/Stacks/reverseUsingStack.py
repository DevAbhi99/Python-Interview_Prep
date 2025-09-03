#Reverse string using stack

class Stack:
    def __init__(self, capacity):
        self.arr=[]
        self.capacity=capacity
    
    def push(self, data):
        if not self.isFull():
            self.arr.append(data)
    
    def pop(self):
        self.arr.pop()
    
    def size(self):
        return len(self.arr)
    
    def top(self):
        return self.arr[len(self.arr)-1]
    
    def isEmpty(self):
        return len(self.arr)==0
    
    def isFull(self):
        return len(self.arr)==self.capacity
    
    def print(self):
        print(self.arr)



s='hello world'

st1=list(s)

st2=Stack(len(st1))

for i in range(0, len(st1)):
    st2.push(st1.pop())


print(''.join(st2.arr))