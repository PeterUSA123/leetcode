# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Example:
# Given "bcabc"
# Return "abc"
#
# Given "cbacdcbc"
# Return "acdb"

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        indexes = {}

        for i in range(len(s) - 1, -1, -1):
            if s[i] in indexes:
                indexes[s[i]].append(i)
            else:
                indexes[s[i]] = [i]

        cList = sorted(indexes.keys())

        result = ''

        while len(result) < len(indexes):
            bottom = min(indexes[c][0] for c in cList)

            candidate = 0

            while indexes[cList[candidate]][-1] > bottom:
                candidate += 1

            result += cList[candidate]

            cList = cList[:candidate] + cList[candidate + 1:]

            for c in cList:
                while indexes[c][-1] < indexes[result[-1]][-1]:
                    indexes[c].pop()
        return result
