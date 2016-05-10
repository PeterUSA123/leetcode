# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n != 0:
            if n % 2 != 0:
                cnt += 1
            n /= 2
        return cnt


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        for i in range(32):
            if n & 1 == 1:
                cnt += 1
            n >>= 1
        return cnt
