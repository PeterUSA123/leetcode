# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        # arr[i] to record the queen is in col#arr[i]&row#i
        arr = [-1 for i in range(n)]

        # to check is the queen put in col#k&row#j is OK
        # arr[i]==j means two queens are in the same col
        # abs(k - i) == abs(arr[i] - j) means two queen are in the same diagonal
        def check(k, j):
            for i in range(k):
                if arr[i] == j or abs(k - i) == abs(arr[i] - j):
                    return False
            return True

        def dfs(depth, valueList):
            # get a solution
            if depth == n:
                ans.append(valueList)
            else:
                for i in range(n):
                    if check(depth, i):
                        arr[depth] = i
                        s = '.' * n
                        dfs(depth + 1, valueList + [s[:i] + 'Q' + s[i + 1:]])

        dfs(0, [])

        return len(ans)