__author__ = 'minyi'
'''Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sval = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        ans = ''
        for i in range(13):
            while num >= val[i]:
                num -= val[i]
                ans +=sval[i]

        return ans
