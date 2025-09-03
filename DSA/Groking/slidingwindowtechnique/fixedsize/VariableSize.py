#Sliding window with variable size


arr=[2,3,1,2,4,3]

target=7


#Algorithm

windowsum=0

left=0

minlen=float('inf')

for right in range(len(arr)):
    windowsum+=arr[right]

    while windowsum>=target:
        minlen=min(minlen, right-left+1)
        windowsum-=arr[left]
        left+=1


if min==float('inf'):
    print(0)
else:
    print(minlen)

