# Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        res = []
        dic = {}
        for i in range(n):
            dic[words[i]] = i

        for word in words:
            word_rev = word[::-1]
            if word_rev in dic and dic[word_rev] != dic[word]:
                res.append([dic[word], dic[word_rev]])
            for i in range(len(word)):
                tmp1 = word[:i][::-1]
                tmp2 = word_rev[:i]
                if tmp1 in dic and self.isPalindrome(word[i:]):
                    res.append([dic[word], dic[tmp1]])
                if tmp2 in dic and self.isPalindrome(word_rev[i:]):
                    res.append([dic[tmp2], dic[word]])
        return res

    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
