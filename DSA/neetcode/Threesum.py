#Find the triplet whose sum equals to 0 and triplets should be distinct

class Solution:
    def threesum(self, nums):
        i=0
        n=len(nums)
        triplet=[]

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            j,k=i+1,n-1

            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    triplet.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return triplet
    

nums=[]

obj=Solution()

print(obj.threesum())
                        
                    
