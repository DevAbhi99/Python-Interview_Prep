#The array nums is given and in arranged in non decreasing order. Remove duplicates from the array and return the number of unique elements

class Solution:
    def removeDuplicates(self, nums):
        k=1
        for i in range(1, len(nums)):
            if nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k+=1
        return k
            




nums=[1,1,2,3,4]

obj=Solution()


print(obj.removeDuplicates(nums))