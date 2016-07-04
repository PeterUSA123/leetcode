__author__ = 'Minyi'
# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return MAX_INT.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647

        if dividend == 0:
            return 0
        if divisor == 0:
            return MAX_INT

        ispositive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        ans, q, dvs = 0, 1, divisor
        while dvs < dividend:
            dvs <<= 1
            q <<= 1

        while dvs >= divisor:
            if dividend >= dvs:
                dividend -= dvs
                ans += q
            q >>= 1
            dvs >>= 1
        ans = ans if ispositive else -ans
        return min(ans, MAX_INT)

s = Solution()
print(s.divide(1,1))
