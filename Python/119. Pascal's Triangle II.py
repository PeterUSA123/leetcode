# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            if i == 0:
                ans[i] = [1]
            elif i == 1:
                ans[i] = [1, 1]
            else:
                ans[i] = [0] * (i + 1)
                ans[i][0] = ans[i][i] = 1
                for j in range(1, i):
                    ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans[rowIndex]
