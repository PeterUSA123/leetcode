__author__ = 'Minyi'
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]


class Solution(object):

    def dfs(self, candidates, target, start, vlist):
        length = len(candidates)
        if target == 0:
            return self.ans.append(vlist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i, vlist + [candidates[i]])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.ans = []
        self.dfs(candidates, target, 0, [])
        return self.ans
