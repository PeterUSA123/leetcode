# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curMax = 0
        curRch = 0

        for i in range(len(nums)):
            if curRch < i:
                curRch = curMax
            curMax = max(curMax, nums[i] + i)

        return curMax > len(nums)