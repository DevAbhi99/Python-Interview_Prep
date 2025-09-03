#ExtractFile name without extension

file='data/abcd.txt'

st=file.split('/')

res=st[len(st)-1].split('.')

print(res[0])
