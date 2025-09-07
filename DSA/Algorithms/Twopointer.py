#Two pointer algorithm

arr=[1,2,4,5,6]

target=6

arr.sort()

i=0
j=len(arr)-1



while(i<j):
    sum=arr[i]+arr[j]

    if sum==target:
        print([i,j])
        break
    elif sum<target:
        i+=1
    else:
        j-=1