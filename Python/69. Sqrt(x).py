# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        ans = float(x)
        while True:
            tmp = ans
            ans = (ans + x / ans) / 2
            if abs(ans - tmp) < 1:
                break
        return int(ans)


s = Solution()
print(s.mySqrt(3))
