# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        if length == 0:
            return [1]
        carry = 0
        digits[length - 1] += 1
        while length > 0:
            digits[length - 1] += carry
            if digits[length - 1] > 9:
                carry = 1
                digits[length - 1] = 0
            else:
                carry = 0
                break
            length -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits
