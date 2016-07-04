# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        area = 0

        while i < len(heights):
            if stack == [] or heights[i] > heights[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                cur = stack.pop()
                if stack == []:
                    width = i
                else:
                    width = i - stack[len(stack) - 1] - 1
                area = max(area, width * heights[cur])
                i -= 1
            i += 1

        while stack != []:
            cur = stack.pop()
            if stack == []:
                width = i
            else:
                width = len(heights) - stack[len(stack) - 1] - 1
            area = max(area, width * heights[cur])

        return area
