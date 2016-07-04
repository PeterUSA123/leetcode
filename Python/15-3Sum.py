__author__ = 'minyi'


# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        lenth = len(nums)
        if lenth < 3:
            return ans

        nums.sort()
        for i in range(lenth):
            target = 0 - nums[i]
            begin = i + 1
            end = lenth - 1
            while begin < end:
                if (nums[begin] + nums[end]) < target:
                    begin += 1
                elif (nums[begin] + nums[end]) > target:
                    end -= 1
                else:
                    tlist = [nums[i], nums[begin], nums[end]]
                    ans.append(tlist)
                    begin += 1

        cans = []
        for list in ans:
            if list not in cans:
                cans.append(list)

        return cans


s = Solution()
print(s.threeSum([0, 0, 0, 0]))
