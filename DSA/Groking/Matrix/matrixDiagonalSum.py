# Given a square matrix (2D array), calculate the sum of its two diagonals.

class Solution:
    def matrixDiagonal(self, nums):
        temp=[]
        row=len(nums)
        col=len(nums[0])
        for i in range(0, row):
            for j in range(0, col):
                if i==j or (i+j==col-1):
                    temp.append(nums[i][j])
        return sum(temp)
    
nums=[[1,2,3],
 [4,5,6],
 [7,8,9]]

obj=Solution()

print(obj.matrixDiagonal(nums))