# Given a binary matrix that has dimensions , consisting of ones and zeros, determine the row that contains the highest number of ones and return two values: the zero-based index of this row and the actual count of ones it possesses.

class Solution:
    def rowWithMaxOne(self, nums):
        row=len(nums)
        col=len(nums[0])
        hm={}
        for i in range(0, row):
            count=0
            for j in range(0, col):
                if nums[i][j]==1:
                    count+=1
                    hm[i]=count
        
        maximum=max(hm.values())

        for k,v in hm.items():
            if v==maximum:
                return [k,v]


nums=[[1, 0], [1, 1], [0, 1]]

obj=Solution()

print(obj.rowWithMaxOne(nums))


