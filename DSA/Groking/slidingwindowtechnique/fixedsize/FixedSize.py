arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

k=5


windowsum=sum(arr[:k])

maximum=0

for i in range(k, len(arr)):
    windowsum+=arr[i]-arr[i-k]
    maximum=max(maximum, windowsum/k)

print(maximum)