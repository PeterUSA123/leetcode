# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        length = 2
        words = set([beginWord])
        wordList.discard(beginWord)
        wordList.discard(endWord)

        while words:
            newwords = set()
            for word in words:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word == endWord:
                            return length
                        if new_word in wordList:
                            newwords.add(new_word)
            words = newwords
            length += 1
            wordList -= words
        return 0
