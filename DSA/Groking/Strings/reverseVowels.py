#Reverse vowels in the string

s='VOWELS'

l=list(s)


#Two pointer algorithm used 

i=0

j=len(l)-1

while(i<j):
    if(l[i].lower() not in  'aeiou'):
        i+=1
        continue
    
    if(l[j].lower() not in 'aeiou'):
        j-=1
        continue
    
    if(l[i].lower() in 'aeiou' and l[j].lower() in 'aeiou'):
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
    
    i+=1
    j-=1


s=''.join(l)

print(s)
