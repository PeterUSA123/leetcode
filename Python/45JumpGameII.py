# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
# ans:目前为止的jump数
#
# curRch:从A[0]进行ret次jump之后达到的最大范围
#
# curMax:从0~i这i+1个A元素中能达到的最大范围
#
# 当curRch < i，说明ret次jump已经不足以覆盖当前第i个元素，因此需要增加一次jump，使之达到记录的curMax
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        curMax = 0
        curRch = 0

        for i in range(len(nums)):
            if curRch < i:
                ans += 1
                curRch = curMax
            curMax = max(curMax, nums[i] + i)

        return ans
