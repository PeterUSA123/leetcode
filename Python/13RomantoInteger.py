__author__ = 'minyi'
'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        ans = dict[s[0]]

        for i in range(1,len(s)):
            if dict[s[i-1]]<dict[s[i]]:
                ans += dict[s[i]] - 2*dict[s[i-1]]
            else:
                ans += dict[s[i]]

        return ans

s = Solution()
print(s.romanToInt())