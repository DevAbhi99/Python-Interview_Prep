import math

#Used two pointer approach

class Solution:
  def sort(self, arr):
    # TODO: Write your code here
    temp=list(arr)
    temp.sort()

    if arr==temp:
      return 0

    i=0
    j=len(arr)-1
    start=0
    end=0

    while(i<j):
      if arr[i]==temp[i]:
        i+=1
      elif arr[j]==temp[j]:
        j-=1
      else:
        start=i
        end=j
        break

    part=arr[start:end+1]

    return len(part)

    
