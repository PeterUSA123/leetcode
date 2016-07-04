# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if len(nums) == 0:
            return res
        elif len(nums) == 1:
            res.append(str(nums[0]))
            return res
        begin = nums[0]
        end = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                end = nums[i]
            else:
                if end == 0:
                    res.append(str(begin))
                else:
                    res.append(str(begin) + "->" + str(end))
                begin = nums[i]
                end = 0
        if not end == 0:
            res.append(str(begin) + "->" + str(end))
        else:
            res.append(str(begin))
        return res
