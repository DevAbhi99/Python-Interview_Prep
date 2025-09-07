#Variable sliding window
arr=[1,2,3,4,5,6,7,8,9,10]



#Find the length with maximum sum


left=0


windowsum=0

minlen=float('inf')



for right in range(len(arr)):
    windowsum+=arr[right]

    while left<right:
        minlen=min(minlen,right-left+1)
        windowsum+=arr[left]
        left+=1

if minlen==float('inf'):
    print(0)
else:
    print(minlen)
        