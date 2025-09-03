#Two dimensional array

arr=[[1,2,3], [4,5,6]]

row=len(arr)

col=len(arr[0])

for i in range(0,row):
    for j in range(0, col):
        if(arr[i][j]%2==0):
            print(arr[i][j])