__author__ = 'Minyi'
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        start = 0
        d = {}

        for i, ch in enumerate(s):
            if ch in d and d[ch] >= start:
                start = d[ch] + 1
            d[ch] = i
            maxLength = max(maxLength,i-start+1)
        return maxLength
