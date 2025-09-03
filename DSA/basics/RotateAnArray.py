#Rotate an array by k steps to the right


arr=[-1,-100,3,99]

k=2


#Algorithm to rotate

if len(arr)==0:
    print(arr)
else:
    k%=len(arr)
    arr=arr[-k:]+arr[:-k]
    print(arr)
    
