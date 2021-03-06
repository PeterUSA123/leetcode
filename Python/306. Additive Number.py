# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
#
# For example:
# "112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
#
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
#
# Follow up:
# How would you handle overflow for very large input integers?

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        import itertools
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            a, b = num[:i], num[i:j]
            if a != str(int(a)) or b != str(int(b)):
                continue
            while j < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, j):
                    break
                j += len(c)
                a, b = b, c
            if j == n:
                return True
        return False


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n / 2 + 1):
            for j in range(1, n - i):
                if self.isValid(i, j, num):
                    return True
        return False

    def isValid(self, i, j, num):
        if num[0] == '0' and i > 1:
            return False
        if num[i] == '0' and j > 1:
            return False
        a, b = int(num[:i]), int(num[i:i + j])
        start = i + j
        while start < len(num):
            b = a + b
            a = b - a
            if not num.startswith(str(b), start):
                return False
            start += len(str(b))
        return True
