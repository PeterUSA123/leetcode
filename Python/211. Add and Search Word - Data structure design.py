# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.wordDict = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(word) in self.wordDict:
            self.wordDict[len(word)].append(word)
        else:
            self.wordDict[len(word)] = [word]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.wordDict:
            return False
        else:
            wordList = self.wordDict[len(word)]
            finalList = [w for w in wordList if self.isMatch(word, w)]
            return len(finalList) > 0

    def isMatch(self, word1, word2):
        """
        return if words is match word2
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        for i in range(len(word1)):
            if word1[i] == '.' or word1[i] == word2[i]:
                continue
            else:
                return False
        return True

        # Your WordDictionary object will be instantiated and called as such:
        # wordDictionary = WordDictionary()
        # wordDictionary.addWord("word")
        # wordDictionary.search("pattern")
