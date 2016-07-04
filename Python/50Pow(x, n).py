# Implement pow(x, n).


# x^n = x ^ (n /2) * x ^(n / 2) (n %2 == 0)或者x^n = x ^ (n /2) * x ^(n / 2) * x(n %2 == 1)。
# n  < 0 的时候，x ^ n =1 / （x ^(-n))
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -1 * n)
        if x == 0:
            return 0.0
        if n == 0:
            return 1.0
        if n == 1:
            return x
        tmp = self.myPow(x,n // 2)
        if n % 2 == 0:
            return tmp*tmp
        else:
            return tmp*tmp * x

s = Solution()
print(s.myPow(0.00001,2147483647))