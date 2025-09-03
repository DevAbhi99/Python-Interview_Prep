# Each element of differenceArray, i.e., differenceArray[i], should be calculated as follows: take the sum of all elements to the left of index i in array nums (let's call it leftSumi), and subtract it from the sum of all elements to the right of index i in array 


class Solution:
    def differenceArray(self, nums):
        dif=[]
        for i in range(0, len(nums)):
                sum1=0
                sum2=0
                for j in range(0,i):
                    sum1+=nums[j]
                for k in range(i+1, len(nums)):
                    sum2+=nums[k]
                dif.append(abs(sum1-sum2))
        return dif

nums=[3, 3, 3]

obj=Solution()

print(obj.differenceArray(nums))
        
