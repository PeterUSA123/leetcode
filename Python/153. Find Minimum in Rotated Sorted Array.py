# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[r]
