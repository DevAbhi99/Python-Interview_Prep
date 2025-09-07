## pointer algorithm

arr=[6,2,4,5,3,1,9]

target=11

#Find indices

temp=list(arr)

temp.sort()

n=len(temp)

i=0

res=[]

for i in range(n-2):
    j,k=i+1,n-1
    while j<k:
        sum=arr[i]+arr[j]+arr[k]

        if(sum==target):
            res.append(arr[i])
            res.append(arr[j])
            res.append(arr[k])
            break
        elif sum<target:
            j+=1
        else:
            k-=1


result=[]

for i in range(len(res)):
    result.append(arr.index(res[i]))


print(result)