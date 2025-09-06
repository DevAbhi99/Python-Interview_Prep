# Use two pointer algorithm


class Solution:
    def waterContainer(self, heights):
        i=0
        j=len(heights)-1
        best=0

        while i<j:
            h=min(heights[i], heights[j])
            best=max(best, h*(j-i))

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return best
    

heights=[]

obj=Solution()

print(obj.waterContainer(heights))
