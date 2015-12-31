# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda interval: interval.start)
        ans = []
        if len(intervals) == 0:
            return []
        tmp = intervals[0]
        for item in intervals:
            if item.start <= tmp.end:
                tmp.end = max(item.end, tmp.end)
            else:
                ans.append(tmp)
                tmp = item
        ans.append(tmp)
        return ans
