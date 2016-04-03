# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        while nums:
            stack = [next(iter(nums))]
            tmp = 0
            while stack:
                tmp += 1
                curr = stack.pop()
                nums.discard(curr)
                if curr - 1 in nums:
                    stack.append(curr - 1)
                if curr + 1 in nums:
                    stack.append(curr + 1)
            res = max(res, tmp)
        return res
