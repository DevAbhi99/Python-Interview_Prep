#Sort the stack using only push and pop operation

class Solution:
    def sortUsingStack(self, stack):
        temp=[]

        while stack:
            x=stack.pop()

            while temp and temp[-1]<x:
                stack.append(temp.pop())

            temp.append(x)

        while temp:
            stack.append(temp.pop())
        
        return stack
    
stack=[4,2,3,1] 

obj=Solution()

print(obj.sortUsingStack(stack))