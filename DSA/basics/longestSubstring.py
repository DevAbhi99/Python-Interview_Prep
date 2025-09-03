#Find the length of the longest substring without repeating the characters

str='abcabcbb'

s=[]

for i in range(0, len(str)):
    if str[i] not in s:
        s.append(str[i])
    else:
        break


print(len(s))
