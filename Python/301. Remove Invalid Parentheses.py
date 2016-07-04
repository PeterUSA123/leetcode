# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return ['']
        left_remove, right_move = 0, 0
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove:
                    left_remove -= 1
                else:
                    right_move += 1
        ans = set()
        self.dfs(0, left_remove, right_move, 0, '', s, ans)
        return list(ans)

    def dfs(self, index, left_remove, right_remove, left_pare, cur, s, ans):
        if left_remove < 0 or right_remove < 0 or left_pare < 0:
            return
        if index == len(s):
            if left_remove == right_remove == left_pare == 0:
                ans.add(cur)
            return

        if s[index] == '(':
            self.dfs(index + 1, left_remove - 1, right_remove, left_pare, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, left_pare + 1, cur + s[index], s, ans)
        elif s[index] == ')':
            self.dfs(index + 1, left_remove, right_remove - 1, left_pare, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, left_pare - 1, cur + s[index], s, ans)
        else:
            self.dfs(index + 1, left_remove, right_remove, left_pare, cur + s[index], s, ans)


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return ['']
        q = {s}
        while q:
            ans = filter(self.isValidParentheses, q)
            if ans: return ans
            q = {cur[:i] + cur[i + 1:] for cur in q for i in xrange(len(cur))}

    def isValidParentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0: return False
                cnt -= 1
        return cnt == 0
