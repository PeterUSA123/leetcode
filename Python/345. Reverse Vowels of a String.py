# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiou'
        size = len(s)

        left, right = 0, size - 1
        ls = list(s)

        while True:
            while left < size and s[left].lower() not in vowels:
                left += 1
            while right >= 0 and s[right].lower() not in vowels:
                right -= 1
            if left >= right:
                break
            ls[left], ls[right] = ls[right], ls[left]
            left += 1
            right -= 1

        return ''.join(ls)


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
