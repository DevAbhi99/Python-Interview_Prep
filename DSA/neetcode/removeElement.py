#Remove val from the given array nums

class Solution:
    def removeElement(self, nums, val):
        t=tuple(nums)
        count=t.count(val)
        for i in range(1, count+1):
            nums.remove(val)
        
        return len(nums)


obj=Solution()

nums=[1,1,2,3,4]
val=1

print(obj.removeElement(nums, val))