# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowLen = len(matrix)
        colLen = len(matrix[0])

        row = [False for i in range(rowLen)]
        col = [False for i in range(colLen)]

        for i in range(rowLen):
            for j in range(colLen):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(rowLen):
            for j in range(colLen):
                if row[i] or col[j]:
                    matrix[i][j] = 0
