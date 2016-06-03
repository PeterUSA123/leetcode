# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
#
# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones, num = 0, 1
        while num <= n:
            ones += (n / num + 8) / 10 * num + (n / num % 10 == 1) * (n % num + 1)
            num *= 10
        return ones


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        m = r = 1
        while n > 0:
            ones += (n + 8) / 10 * m + (n % 10 == 1) * r
            r += n % 10 * m
            m *= 10
            n /= 10
        return ones

        # For example '8192':
        # 1-999 -> countDigitOne(999)
        # 1000-1999 -> 1000 of 1s + countDigitOne(999)
        # 2000-2999 -> countDigitOne(999)
        # .
        # .
        # 7000-7999 -> countDigitOne(999)
        # 8000-8192 -> countDigitOne(192)
        # Count of 1s : countDigitOne(999)*8 + 1000 + countDigitOne(192)
        # Noticed that, if the target is '1192':
        # Count of 1s : countDigitOne(999)*1 + (1192 - 1000 + 1) + countDigitOne(192)
        # (1192 - 1000 + 1) is the 1s in thousands from 1000 to 1192.
