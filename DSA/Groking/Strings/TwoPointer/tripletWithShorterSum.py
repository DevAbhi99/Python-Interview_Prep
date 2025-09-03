arr=[-1, 4, 2, 1, 3]

arr.sort()

target=5

i=0

n=len(arr)

count=0

for i in range(n-2):
    j=i+1
    k=n-1
    while(j<k):
        sum=arr[i]+arr[j]+arr[k]
        if sum<target:
            count+=(abs(j-k))
            j+=1
        else:
            k-=1
            
print(count)
            