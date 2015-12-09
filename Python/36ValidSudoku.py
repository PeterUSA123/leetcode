__author__ = 'Minyi'
# he Sudoku board could be partially filled, where empty cells are filled with the character '.'.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row
        i = 0
        while i < 9:
            j = 0;
            d = {}
            while j < 9:
                if board[i][j] != '.' and board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
                j += 1
            i += 1

        # column
        j = 0
        while j < 9:
            i = 0
            d = {}
            while i < 9:
                if board[i][j] != '.' and board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
                i += 1
            j += 1

        # s-board
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                m = 0
                d = {}
                while m < 3:
                    n = 0
                    while n < 3:
                        if board[i + m][j + n] != '.' and board[i + m][j + n] in d:
                            return False
                        else:
                            d[board[i + m][j + n]] = True
                        n += 1
                    m += 1
                j += 3
            i += 3
        return True
