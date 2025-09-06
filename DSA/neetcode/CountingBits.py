class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]

        for i in range(0,n+1):
            temp=format(i,'b')
            t=tuple(temp)
            res.append(t.count('1'))
 
        return res

        