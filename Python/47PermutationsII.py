# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].


# 给出一个排列情况，输出下一个排列的结果，然后将其append到结果里面输出 #31
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not len(nums):
            return

        index = len(nums) - 2

        while index >= 0 and nums[index] >= nums[index + 1]:
            index -= 1

        if index >= 0:
            i = index + 1
            while i < len(nums) and nums[i] > nums[index]:
                i += 1
            nums[i - 1], nums[index] = nums[index], nums[i - 1]

        left, right = index + 1, len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        tmp = nums[:]
        ans = []
        ans.append(nums)
        while True:
            tmp = self.nextPermutation(tmp)
            if tmp != nums:
                t = tmp[:]
                ans.append(t)
            else:
                break
        return ans
