__author__ = 'Minyi'
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#For example, given n = 3, a solution set is:
#"((()))", "(()())", "(())()", "()(())", "()()()"

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n > 0:
            self.gen(n, n, "", result)
        return result

    def gen(self, left, right, s, ans):
        if left > right or left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            ans.append(s)
            return
        if left:
            self.gen(left - 1, right, s + '(', ans)
        if right:
            self.gen(left, right - 1, s + ')', ans)


s = Solution()
print(s.generateParenthesis(1))
