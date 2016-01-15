# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1
        dict = [[0 for i in range(len2+1)] for j in range(len1+1)]

        for j in range(1,len2+1):
            dict[0][j] = j

        for i in range(1,len1+1):
            dict[i][0] = i

        if word1[0] != word2[0]:
            dict[1][1] = 1

        if len1 >= 1 and len2 >= 1:
            for i in range(1, len1+1):
                for j in range(1, len2+1):
                    dict[i][j] = min(dict[i - 1][j] + 1,
                                     dict[i][j - 1] + 1, dict[i - 1][j - 1] + int(word1[i-1] != word2[j-1]))

        return dict[len1][len2]


s = Solution()
print(s.minDistance("a", "b"))
