#Reverse the words in string and not the characters

s='Python is awesome'  #output should be Awesome is python 

st=s.split(' ')

st.reverse()

st[0]=st[0].capitalize()

st[len(st)-1]=st[len(st)-1].lower()

s=' '.join(st)


print(s)