#Sliding window of fixed window size

arr=[1,2,3,4,5,6,7,8,9,10]

k=3

#Find the maximum sum

windowsum=sum(arr[:k])

maxsum=0

for i in range(k, len(arr)):
    windowsum+=arr[i]-arr[i-k]
    maxsum=max(maxsum,windowsum)


print(windowsum)