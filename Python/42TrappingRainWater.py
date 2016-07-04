# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        secHeight = 0
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            if height[left] < height[right]:
                secHeight = max(height[left], secHeight)
                area += secHeight - height[left]
                left += 1
            else:
                secHeight = max(height[right], secHeight)
                area += secHeight - height[right]
                right -= 1;

        return area
