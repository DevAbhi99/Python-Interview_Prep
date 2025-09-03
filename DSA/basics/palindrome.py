#To check if a string is palindrome

s='yooy'

chars=list(s)

chars.reverse()

st=''.join(chars)

if st==s:
    print('Palindrome!')
else:
    print('Not palindrome!')