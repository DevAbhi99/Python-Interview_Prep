#Replace all vowels with *

s='abcdefghijklmnopqrstuvwxyz'

for i in range(0, len(s)):
    if s[i] in 'aeiouAEIOU':
        s=s.replace(s[i], '*')


print(s)