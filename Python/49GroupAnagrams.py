# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


# 把字符串排好序的结果作为key，同一个key的字符串组成的队列作为value，构建一个字典。然后将字典的value排序，append到结果返回。
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_arr, ans = {}, []

        for str in strs:
            sort_str = ''.join(sorted(str))
            if sort_str in dict_arr:
                dict_arr[sort_str] += [str]
            else:
                dict_arr[sort_str] = [str]

        for key in dict_arr:
            tmp = dict_arr[key]
            tmp.sort()
            ans += [tmp]
        return ans
