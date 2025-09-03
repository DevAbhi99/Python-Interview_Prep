# Find the shortest distance between two words

words=["a", "c", "d", "b", "a"]

word1='a'

word2='b'


position1=-1

position2=-1

minDistance=len(words)

#Algorithm

for i in range(0, len(words)):
    if words[i]==word1:
        position1=i
    if words[i]==word2:
        position2=i
    if position1!=-1 and position2!=-1:
        minDistance=min(minDistance, abs(position1-position2))

print(minDistance)

