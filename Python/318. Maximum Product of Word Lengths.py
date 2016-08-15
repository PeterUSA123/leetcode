# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
#
# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".
#
# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".
#
# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxlen = {}

        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            if mask in maxlen:
                maxlen[mask] = max(maxlen[mask], len(word))
            else:
                maxlen[mask] = len(word)

        result = 0
        for n in maxlen:
            for m in maxlen:
                if not (n & m):
                    result = max(result, maxlen[n] * maxlen[m])
        return result


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        curr_max = 0
        while words:
            curr_word = set(words[0])
            curr_len = len(words[0])

            words = words[1:]
            for word in words:
                for c in curr_word:
                    if c in word:
                        break
                else:
                    curr_max = max(curr_max, curr_len * len(word))
        return curr_max
