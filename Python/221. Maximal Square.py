# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        maxcnt = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = ord(matrix[i][0]) - ord('0')
            maxcnt = max(maxcnt, dp[i][0])
        for j in range(n):
            dp[0][j] = ord(matrix[0][j]) - ord('0')
            maxcnt = max(maxcnt, dp[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    l1 = dp[i][j - 1]
                    l2 = dp[i - 1][j]
                    if l1 != l2:
                        dp[i][j] = min(l1, l2) + 1
                    else:
                        dp[i][j] = l1 + 1 if matrix[i - l1][j - l1] == '1' else l1
                maxcnt = max(maxcnt, dp[i][j])
        return maxcnt * maxcnt
