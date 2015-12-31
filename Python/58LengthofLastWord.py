# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        first = True

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and first:
                continue
            elif s[i] != ' ':
                first = False
                ans += 1
            else:
                break
        return ans


s = Solution()
print(s.lengthOfLastWord(" a hdjsh "))
