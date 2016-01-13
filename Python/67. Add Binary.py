# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        if len_a == 0:
            return b
        if len_b == 0:
            return a
        ans = ""
        carry = 0
        while len_a > 0 and len_b:
            tmp = int(a[len_a - 1]) + int(b[len_b - 1]) + carry
            carry = tmp // 2
            tmp %= 2
            ans += str(tmp)
            len_a -= 1
            len_b -= 1
        if len_a == 0:
            while len_b > 0:
                tmp = int(b[len_b - 1]) + carry
                carry = tmp // 2
                tmp %= 2
                ans += str(tmp)
                len_b -= 1
        if len_b == 0:
            while len_a > 0:
                tmp = int(a[len_a - 1]) + carry
                carry = tmp // 2
                tmp %= 2
                ans += str(tmp)
                len_a -= 1
        if carry == 1:
            ans += str(carry)
        ans = ans[::-1]
        return ans
