__author__ = 'minyi'
#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
#Return the sum of the three integers. You may assume that each input would have exactly one solution.

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lenth = len(nums)

        nums.sort()
        goal = 2**31-1
        first = True
        for i in range(lenth):
            begin = i+1
            end = lenth - 1
            while begin < end:
                total = nums[i]+nums[begin]+nums[end]
                if(first):
                    ans = total
                    first = False
                else:
                    if abs(total-target) < abs(ans-target):
                        ans = total
                if ans==target:
                    return ans
                if total <target:
                    begin += 1
                else:
                    end -= 1

        return ans

s = Solution()
print(s.threeSumClosest([1,1,1,0],-100))