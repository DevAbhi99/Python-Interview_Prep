import math

class Solution:
  def searchTriplet(self, arr, target_sum):
    # TODO: Write your code here
    arr.sort()
    n=len(arr)
    i=0
    bestSum=None
    bestDif=float('inf')

    for i in range(n-2):
      j,k=i+1,n-1
      while j<k:
        sums=arr[i]+arr[j]+arr[k]
        dif=abs(target_sum-sums)
        if dif<bestDif or (dif==bestDif and (sums<bestSum or bestSum is None)):
          bestDif=dif
          bestSum=arr[i]+arr[j]+arr[k]
          if bestDif==0:
            return bestSum
        elif sums<target_sum:
          j+=1
        else:
          k-=1
    return bestSum



    
obj=Solution()

nums=[1,2,3,4,5,6]

target=20

print(obj.searchTriplet(nums, target))