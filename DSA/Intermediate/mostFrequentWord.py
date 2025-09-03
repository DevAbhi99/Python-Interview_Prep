#Find the most frequent word

s='hi bro how is going bro'

st=s.split(' ')

hm={} #map or a dictionary to count the frequency of the words in the string


for i in range(0, len(st)):
    if st[i] in hm:
        hm[st[i]]+=1
    else:
        hm[st[i]]=1


#Finding the maximum value

maximum=max(hm.values())

for k,v in hm.items():
    if v==maximum:
        print('Most frequently used word is',k,'with frequency',v)
        break


        