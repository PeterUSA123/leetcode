__author__ = 'Minyi'
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# 用一个bool数组来标记已经匹配过的字符，找到最长的连续标记的长度就是所求的结果。只要遍历两遍数组，时间复杂度为O(n)。

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = [False]*len(s)
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')' and stack:
                flag[i] = True
                flag[stack[len(stack)-1]] = True
                stack.pop()

        maxLen,curLen = 0,0
        for i in range(len(s)):
            if flag[i]:
                curLen += 1
            else:
                curLen = 0
            maxLen = max(maxLen,curLen);

        return maxLen

s = Solution()
print(s.longestValidParentheses("())"))



