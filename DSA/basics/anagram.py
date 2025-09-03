# Check if two strings are anagram or not

s1='silent'

s2='listen'

if len(s1)!=len(s2):
    print('Not an anagram')



ns1=list(s1)

ns2=list(s2)

ns1.sort()

ns2.sort()


flag=0

for i in range(0, len(ns1)):
    if(ns1[i]==ns2[i]):
        flag+=1


if flag==len(ns1):
    print('Two strings are anagram')
else:
    print('Two strings are not anagram')