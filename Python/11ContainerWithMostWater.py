__author__ = 'minyi'
'''Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        ans = 0
        while left < right:
            tmp = min(height[left],height[right]) * (right-left)
            if ans < tmp:
                ans = tmp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans