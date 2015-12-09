__author__ = 'Minyi'
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        for i in range(n - 1):
            letter, tmp, cnt = ans[0], '', 0
            for char in ans:
                if letter == char:
                    cnt += 1
                else:
                    tmp += str(cnt) + letter
                    letter = char
                    cnt = 1
            tmp += str(cnt) + letter
            ans = tmp
        return ans
