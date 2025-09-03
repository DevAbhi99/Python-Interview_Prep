# Given an array of integers nums, return the number of good pairs in it. A pair (i, j) is called good if nums[i] == nums[j] and i < j.

nums=[1,1,1,1]

count=0

#Brute force approach
for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):
        if(nums[i]==nums[j]):
            count+=1

print(count)

#Time complexity O(n^2)


#Optimized approach uses hashmap


seen={}

pairs=0

for x in nums:
    c=seen.get(x,0)
    pairs+=c
    seen[x]=c+1

print(pairs)

#Time complexity O(n)