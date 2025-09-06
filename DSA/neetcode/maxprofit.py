class Solution:
    def maxProfit(prices):
        i,j=0,1
        profit=0

        while(j<len(prices)):
            if prices[j]>prices[i]:
                profit=max(profit, prices[j]-prices[i])
            else:
                i=j
            j+=1

        return profit

obj=Solution()

prices=[]

print(obj.maxProfit(prices))
