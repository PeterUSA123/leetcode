__author__ = 'Minyi'
# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0;
        ans = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans += 1

        return ans
