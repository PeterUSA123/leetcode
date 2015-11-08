__author__ = 'Minyi'
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
        	return ''
        if len(strs)==1:
            return strs[0]
        lenth = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i])<lenth:
                lenth = len(strs[i])
            if lenth == 0:
                return ''
            ans = strs[0][:lenth]
            for j in range(lenth):
                if ans[j] != strs[i][j]:
                    ans = ans[:j]
                    lenth = j
                    break
        return ans

s = Solution()
print(s.longestCommonPrefix(["c","acc","ccc"]))
