#Implementation of stack

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


st=Stack(5)

st.push(1)

st.push(2)

st.push(3)

st.push(4)

st.push(5)

st.push(6)

st.print()