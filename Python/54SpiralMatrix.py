# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

# 在定义递归时用(x1,y1), (x2,y2)来限制当前考虑矩阵的左上角和右下角
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        if not matrix:
            return ans
        n, m = len(matrix), len(matrix[0])

        self.getOrder(matrix, 0, 0, n - 1, m - 1, ans)

        return ans

    def rec(self, matrix, x1, y1, x2, y2, ans):
        dict_x = x2 - x1 + 1
        if x1 > x2 or y1 > y2:
            return
        # empty
        if dict_x <= 0:
            return
        # single row
        if dict_x == 1:
            for j in range(y1, y2 + 1):
                ans.append(matrix[x1][j])
            return

        dict_y = y2 - y1 + 1
        # single col
        if dict_y == 1:
            for i in range(x1, x2 + 1):
                ans.append(matrix[i][y1])
            return

        for j in range(y1, y2):
            ans.append(matrix[x1][j])

        for i in range(x1, x2):
            ans.append(matrix[i][y2])

        for j in range(y2, y1, -1):
            ans.append(matrix[x2][j])

        for i in range(x2, x1, -1):
            ans.append(matrix[i][y1])

        self.rec(matrix, x1 + 1, y1 + 1, x2 - 1, y2 - 1, ans)
