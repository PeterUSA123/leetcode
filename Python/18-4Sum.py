__author__ = 'minyi'


# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lenth = len(nums)
        if lenth < 4:
            return []
        dict = {}
        res = set()
        nums.sort()
        for i in range(lenth):
            for j in range(i + 1, lenth):
                if nums[i] + nums[j] not in dict:
                    dict[nums[i] + nums[j]] = [(i, j)]
                else:
                    dict[nums[i] + nums[j]].append((i, j))

        for i in range(lenth):
            for j in range(i + 1, lenth - 2):
                tmp = target - nums[i] - nums[j]
                if tmp in dict:
                    for k in dict[tmp]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))

        return [list(i) for i in res]
