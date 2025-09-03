#Find the longest common substring of two strings

s1='aabcdee'

s2='oabcdoo'

minLength=min(len(s1), len(s2))

st=[]

for i in range(0, minLength):
    if s1[i]==s2[i]:
        if s1[i] not in st:
            st.append(s1[i])


print('The longest common substring is',''.join(st))