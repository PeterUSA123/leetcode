# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Related problem: Reverse Integer

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        cnt = 0
        while n != 0:
            ans = ans * 2 + n % 2
            n /= 2
            cnt += 1
        if cnt < 32:
            ans = ans * pow(2, 32 - cnt)
        return ans


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        oribin = '{0:032b}'.format(n)
        reversebin = oribin[::-1]
        return int(reversebin, 2)
