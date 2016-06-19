# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


# 数论
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math

        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        for i in range(int(math.sqrt(n)) + 1):
            tmp = int(math.sqrt(n - i * i))
            if tmp * tmp + i * i == n:
                if tmp > 0 and i > 0:
                    return 2
                elif tmp > 0 or i > 0:
                    return 1
                else:
                    return 0
        return 3


# DP TL
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import collections

        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]


# DP AC
class Solution(object):
    _dp = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]
