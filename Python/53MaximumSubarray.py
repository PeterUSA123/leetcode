# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.


# dp
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        max_sum = nums[0]

        for i in range(len(nums)):
            ans = max(ans+nums[i],nums[i])
            max_sum = max(ans,max_sum)
        return  max_sum