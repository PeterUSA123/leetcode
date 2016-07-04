__author__ = 'minyi'
__author__ = 'minyi'
"""
 '.' Matches any single character.; '*' Matches zero or more of the preceding element.; The matching should cover the entire input string (not partial).; The function prototype should be: bool isMatch(const char *s, const char *p) Some examples:
isMatch("aa","a") ¡ú false
isMatch("aa","aa") ¡ú true
isMatch("aaa","aa") ¡ú false
isMatch("aa", "a*") ¡ú true
isMatch("aa", ".*") ¡ú true
isMatch("ab", ".*") ¡ú true
isMatch("aab", "c*a*b") ¡ú true
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        #build the matrix d[x][y] to record whether the s[:x] and p[:y] is matching
        dp = [[True]+[False]*m]
        for i in range(n):
            dp.append([False]*(m+1))


        for i in range(1,n+1):
            x = p[i-1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in range(1, m+1):
                if x == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and p[i-2] == s[j-1]) or (dp[i][j-1] and p[i-2]=='.')
                elif x == '.' or x == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[n][m]
