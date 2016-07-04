__author__ = 'minyi'
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        range = [-1,-1]

        while(left < right):
            mid = left+(right-left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return range
        range[0] = left

        # Search for upper bound
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid]> target:
                right = mid
            else:
                left = mid + 1
        range[1] = right - 1

        return range

s = Solution()
print(s.searchRange([1,2],1))
