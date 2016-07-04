__author__ = 'Minyi'
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = '@#' + '#'.join(s) + '#%'
        p = [0]*4010
        mx, id, mLen, right = 0,0,0,0
        for i in range(1,len(t)-1):
            if mx > i:
                p[i] = min(p[2*id-i],mx-i)
            else:
                p[i] = 1
            while t[i + p[i]] == t[i - p[i]]:
                p[i] += 1
            if i+ p[i] > mx:
                mx = i + p[i]
                id = i
            if mLen < p[i]:
                mLen = p[i]
                right = i
        return s[right//2 - mLen//2: right//2 - mLen//2 + mLen - 1]