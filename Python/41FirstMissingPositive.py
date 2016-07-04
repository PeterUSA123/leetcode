__author__ = 'minyi'


# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.

#*Bucket sort

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 1

        for i in range(len(nums)):
            while (nums[i] != (i + 1)) and (nums[i] > 0) and (nums[i] <= (len(nums))) and (nums[i] != nums[nums[i] - 1]):
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp

        for i in range(len(nums)):
            if nums[i] != (i + 1):
                return i + 1
        return len(nums) + 1
