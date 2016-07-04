# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.

# https://www.hrwhisper.me/leetcode-game-of-life/

class Solution(object):
    def countLiveNeighbors(self, i, j, m, n, board):
        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        cnt = 0
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
            if board[nx][ny] == 1 or board[nx][ny] == 2: cnt += 1

        return cnt

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = self.countLiveNeighbors(i, j, m, n, board)
                if board[i][j]:
                    if not (cnt == 2 or cnt == 3):  board[i][j] = 2
                else:
                    if cnt == 3: board[i][j] = 3

        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] & 1
