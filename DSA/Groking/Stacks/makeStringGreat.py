#Make string great

s='AaBCcdEeff'


temp=[]

for i in range(1, len(s)):
    if s[i]==s[i].upper() and s[i-1]==s[i].lower() or s[i]==s[i].lower() and s[i-1]==s[i].upper():
        continue
    else:
        temp.append(s[i])

print(temp)
