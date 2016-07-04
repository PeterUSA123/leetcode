__author__ = 'minyi'
#Determine whether an integer is a palindrome. Do this without extra space.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        str_value = str(x)

        i=0
        while i<len(str_value):
            if str_value[i] != str_value[len(str_value)-1-i]:
                return False
            i += 1
        return True
