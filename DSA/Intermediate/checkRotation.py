#To check if two strings are rotation of one another

w1='erbottlewat'

w2='waterbottle'


if(len(w1)!=len(w2)):
    print('Not a rotation')

nw1=list(w1)

nw2=list(w2)


nw1.sort()

nw2.sort()

flag=0

for i in range(0, len(nw1)):
    if nw1[i]==nw2[i]:
        flag+=1


if flag==len(nw1):
    print('Both are rotations')
else:
    print('Both are not rotations')