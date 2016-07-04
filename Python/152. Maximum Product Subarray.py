# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_tmp = nums[0]
        min_tmp = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            a = max_tmp * nums[i]
            b = min_tmp * nums[i]
            max_tmp = max(max(a, b), nums[i])
            min_tmp = min(min(a, b), nums[i])
            ans = max_tmp if max_tmp > ans else ans
        return ans
