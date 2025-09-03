#Given a one-dimensional array of integers, create a new array that represents the running sum of the original array.

class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i]=nums[i-1]+nums[i]
        return nums


nums=[2, 3, 5, 1, 6]

obj=Solution()

print(obj.runningSum(nums))