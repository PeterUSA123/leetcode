__author__ = 'Minyi'
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match_dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        ans = []
        for char in s:
            if char in ['(', '[', '{']:
                ans.append(char)
            elif ans:
                ch = ans.pop()
                if match_dic[ch] != char:
                    return False
            else:
                return False
        if ans:
            return False
        return True

s = Solution()
print(s.isValid(']'))
