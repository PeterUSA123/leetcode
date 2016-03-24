# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0

        sums = [0 for i in range(len(triangle))]
        sums[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i]) - 1, -1, -1):
                if j == len(triangle[i]) - 1:
                    sums[j] = sums[j - 1] + triangle[i][j]
                elif j == 0:
                    sums[j] = sums[j] + triangle[i][j]
                else:
                    sums[j] = min(sums[j - 1], sums[j]) + triangle[i][j]
        return min(sums)
