__author__ = 'Minyi'
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        postive = True
        if x < 0:
            postive = False
        x = abs(x)
        ans = 0
        max = 0x7fffffff
        min = 0x80000000
        while x!=0:
            ans = ans*10 + x%10
            if ans > 2 ** 31 - 1:
                return 0
            x //= 10
        if not postive:
            return -1*ans
        return ans