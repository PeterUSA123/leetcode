# Given an array of integers, every element appears twice except for one. Find that single one.

from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x^y, nums)