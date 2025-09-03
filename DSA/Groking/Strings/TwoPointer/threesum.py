#Find the indexes of triplets which sums upto the target


class Solution:
    def tripleSum(self, nums, target):
        nums.sort()
        i=0
        j=1
        k=len(nums)-1
        flag=0
        res=[]

        while(j<k):
            sum=nums[i]+nums[j]+nums[k]
            if sum==target:
                res.append([i,j,k])
                flag=1
                j+=1
                k-=1
            elif sum<target:
                j+=1
            else:
                k-=1

        if flag==1:
            return res
        
        return [-1,-1,-1]
    
obj=Solution()

nums=[1,2,3,4,5,6]

target=7


print(obj.tripleSum(nums, target))

