# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# Note: Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        ans = 0
        num = 0
        sign = 1
        stack = [1]

        for ch in s + '+':
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-':
                ans += num * sign * stack[-1]
                sign = 1 if ch == '+' else -1
                num = 0
            elif ch == '(':
                stack.append(sign * stack[-1])
                sign = 1
            elif ch == ')':
                ans += num * sign * stack[-1]
                num = 0
                stack.pop()
        return ans
