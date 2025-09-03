#Find the next greater element

nums=[4,5,2,25]

#Brute force method

res=[]

for i in range(len(nums)):
    temp=-1
    for j in range(i+1, len(nums)):
        if nums[j]>nums[i]:
            temp=nums[j]
            break
    res.append(temp)

print(res)
