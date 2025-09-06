class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums=list(set(nums))

        nums.sort()

        best=1
        curr=1

        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                curr+=1
            else:
                best=max(best, curr)
                curr=1

        return max(best, curr)



obj=Solution()

nums=[]

print(obj.longestConsecutive(nums))

