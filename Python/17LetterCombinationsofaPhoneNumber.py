__author__ = 'minyi'
#Given a digit string, return all possible letter combinations that the number could represent.
#A mapping of digit to letters (just like on the telephone buttons) is given below.
#Input:Digit string "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

import copy
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        str = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        ans = []
        for char in digits:
            if len(ans)==0:
                for ch in str[ord(char)-ord('0')]:
                    ans.append(ch)
            else:
                tmp = copy.deepcopy(ans)
                for i in range(len(tmp)):
                    for ch in str[ord(char)-ord('0')]:
                        ans.append(tmp[i]+ch)
                for s in tmp:
                    ans.remove(s)


        return ans

s = Solution()
print(s.letterCombinations("23"))




