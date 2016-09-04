# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i * i <= num:
            if num / i * i == num and num / i == i:
                return True
            i += 1
        return False


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # newton menthod
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # newton menthod
        r = num
        while r * r > num:
            r = (r + num / r) / 2
        return r * r == num
