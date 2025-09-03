#Find frequency of each character in a string

s='abbcccddddeeeee'


hm={}

for i in range(0, len(s)):
    if s[i] in hm:
        hm[s[i]]+=1
    else:
        hm[s[i]]=1


for k,v in hm.items():
    print('The frequency for',k,'is',v)