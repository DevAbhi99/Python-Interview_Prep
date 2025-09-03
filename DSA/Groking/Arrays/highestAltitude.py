# A bike rider is going on a ride. The road contains n + 1 points at different altitudes. The rider starts from point 0 at an altitude of 0. Given an array of integers gain of length n, where gain[i] represents the net gain in altitude between points i and i + 1 for all (0 <= i < n), return the highest altitude of a point.


class Solution:
    def highestAltitude(self, nums):
        maxAltitude=0
        for i in range(1, len(nums)):
            nums[i]=nums[i-1]+nums[i]
        maxAltitude=max(0, max(nums))
        return maxAltitude
        



nums=[4, -3, 2, -1, -2]

obj=Solution()

print(obj.highestAltitude(nums))

