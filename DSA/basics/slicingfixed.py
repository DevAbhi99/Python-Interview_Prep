#Extracting fixed word


s='abcdefghij'

word='cde'

if word not in s:
    print('word doesnt exist')

index=s.find(word)

length=len(word)

print(s[index:length+2])