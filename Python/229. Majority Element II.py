# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
#
# Hint:
#
# How many majority elements could it possibly have?

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

        res = []
        for n, cnt in dic.items():
            if cnt > len(nums) // 3:
                res.append(n)
        return res
