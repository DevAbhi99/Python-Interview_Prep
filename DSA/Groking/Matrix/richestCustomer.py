# You are given an m x n matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.

class Solution:
    def richestCustomer(self, nums):
        temp=[]
        row=len(nums)
        col=len(nums[0])
        for i in range(0, row):
            sum=0
            for j in range(0, col):
                sum+=nums[i][j]
                temp.append(sum)
        return max(temp)


nums=[[5,10,15],
  [10,20,30],
  [15,30,45]]

obj=Solution()

print(obj.richestCustomer(nums))
