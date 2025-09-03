#Given a sorted array return the two indices at which the elements add upto the target


class Solution:
    def twoSum(self, nums, target):
        #Optimized approach :- Using two pointer algorithm
        i=0
        j=len(nums)-1

        while(i<j):
            sum=nums[i]+nums[j]
            
            if sum==target:
                return [i,j]
            elif sum<target:
                i+=1
            else:
                j-=1
            
            i+=1
            j-=1


obj=Solution()

nums=[1,2,3,4,5,6]

target=6

print(obj.twoSum(nums, target))

