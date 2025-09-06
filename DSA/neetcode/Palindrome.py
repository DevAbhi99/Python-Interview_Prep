class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned=''.join(ch for ch in s if ch.isalnum() or ch.isspace())

        l1=''.join(cleaned.lower().split(' '))

        temp=list(l1)

        temp.reverse()

        l2=''.join(temp)

        return l1==l2
        