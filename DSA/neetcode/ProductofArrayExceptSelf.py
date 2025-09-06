import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output=[]

        
        for i in range(len(nums)):
            l=list(nums)
            l.remove(nums[i])
            output.append(math.prod(l))

        return output
