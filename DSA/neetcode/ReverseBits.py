class Solution:
    def reverseBits(self, n: int) -> int:
        binary=format(n, '032b')
        temp=list(binary)
        temp.reverse()
        temp=''.join(temp)
        return int(temp,2)

        