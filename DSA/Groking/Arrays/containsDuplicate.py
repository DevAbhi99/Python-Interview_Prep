#To check if an array has duplicate values or not

class Solution:
    def containsDuplicate(self, nums):
        hm={}
        for i in range(0, len(nums)):
            if nums[i] in hm:
                hm[nums[i]]+=1
            else:
                hm[nums[i]]=1
        
        if max(hm.values())==1:
            return True
        
        return False
    

nums=[1,2,3,4,5]

obj=Solution()

print(obj.containsDuplicate(nums))

