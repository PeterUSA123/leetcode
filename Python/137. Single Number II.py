# Given an array of integers, every element appears three times except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return nums[0]
        nums.sort()
        for i in range(0, len(nums), 3):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = sum(nums)
        sum2 = 3*sum(list(set(nums)))
        return (sum2 - sum1) / 2