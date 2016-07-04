# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].

class Solution(object):
    def check(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if s == '':
            return True
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[len(s)]

    def dfs(self, s, dict, stringlist):
        if self.check(s, dict):
            if len(s) == 0:
                Solution.ans.append(stringlist[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in dict:
                    self.dfs(s[i:], dict, stringlist + ' ' + s[:i])

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        Solution.ans = []
        self.dfs(s, wordDict, '')
        return Solution.ans


s = Solution()
print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
