# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        tmp = 5
        while n >= tmp:
            ans += n / tmp
            tmp *= 5
        return ans


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n != 0:
            ans += n / 5
            n /= 5
        return ans
