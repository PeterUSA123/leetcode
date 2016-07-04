# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].


# 刚开始的思路是先将nums[:n - 1]的所有情况输出，然后这些结果，每个在不同的位置插入最后一个数。
class Solution(object):
    def solve(self, nums, n):
        if n == 0:
            return [[nums[0]]]
        else:
            arr = self.solve(nums, n - 1)
            ans = []
            for i in arr:
                for j in range(len(i) + 1):
                    tmp = i[:]
                    tmp.insert(j, nums[n])
                    ans.append(tmp)
            return ans

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) == 0:
            return []
        else:
            return self.solve(nums, len(nums) - 1)
