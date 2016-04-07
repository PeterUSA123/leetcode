# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [(i - 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                tmp = s[j:i]
                if tmp == tmp[::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]
