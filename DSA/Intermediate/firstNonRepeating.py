#Find the first non repeating character in a string

a='swiss'

hm={} #hashmap

for i in range(0, len(a)):   #Stored the frequency of every character in a string
    if a[i] in hm:
        hm[a[i]]+=1
    else:
        hm[a[i]]=1


for i in range(0, len(a)):   #Using the character has a key retrieved the value of the corresponding key and then if the value is equal to 1 then thats the non repeating character and break the loop
    if hm[a[i]]==1:
        print(a[i])
        break





