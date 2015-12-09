__author__ = 'Minyi'
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.


class Solution(object):
    def isValid(self, board, x, y):
        # row
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False

        # column
        for j in range(9):
            if j != x and board[x][j] == board[x][y]:
                return False
        # s-board
        m, n = 3 * (x // 3), 3 * (y // 3)
        for i in range(3):
            for j in range(3):
                if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                    return False
        return True

    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i][j] = k
                        if self.isValid(board, i, j) and self.dfs(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
