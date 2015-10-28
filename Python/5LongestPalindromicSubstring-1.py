__author__ = 'Minyi'
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        table = [[0 for x in range(n)] for x in range(n)]
        maxLen = 0
        begin = 0

        for i in range(0,n):
            table[i][i] = True

        for i in range(0,n-1):
            if s[i]==s[i+1]:
                table[i][i+1] = True
                begin = i
                maxLen = 2

        for k in range(3,n+1):
            for i in range(0,n-k+1):
                j = i+k-1
                if s[i]==s[j] and table[i+1][j-1]:
                    table[i][j] = True
                    begin = i
                    maxLen = k
        return s[begin:maxLen+1]