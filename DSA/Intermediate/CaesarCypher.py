# Shift the characters by kth position

s='abcdefc'

k=3

if len(s)==0:
    print(s)
else:
    s=list(s)
    length=len(s)
    k=k%length
    print(''.join(s[-k:]+s[:-k]))






