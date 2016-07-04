# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        i = 0
        while i < len(words):
            size = 0
            begin = i
            while i < len(words):
                if size == 0:
                    newsize = len(words[i])
                else:
                    newsize = size + len(words[i]) + 1
                if newsize <= maxWidth:
                    size = newsize
                else:
                    break
                i += 1
            spaceCnt = maxWidth - size
            if i - begin - 1 > 0 and i < len(words):
                everyCount = spaceCnt // (i - begin - 1)
                spaceCnt %= i - begin - 1
            else:
                everyCount = 0
            j = begin;s=""
            while j < i:
                if j == begin:
                    s = words[j]
                else:
                    s += ' ' * (everyCount + 1)
                    if spaceCnt > 0 and i < len(words):
                        s += ' '
                        spaceCnt -= 1
                    s += words[j]
                j += 1
            s += ' ' * spaceCnt
            ans.append(s)
        return ans


s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
