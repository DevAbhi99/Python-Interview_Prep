#Check if the string is panagram that is if every character in the string is Pangram

s='How vexingly quick daft zebras jump!'

cleaned=''.join(ch for ch in s if ch.isalnum() or ch.isspace())

print(cleaned)

temp='abcdefghijklmnopqrstuvwxyz'

l=[]

for i in range(0, len(cleaned)):
        l.append(s[i].lower())


l.sort()


s=set(l)

nl=list(s)

nl.sort()

if ''.join(nl).strip()==temp:
    print('Panagram')
else:
    print('Not panagram')



