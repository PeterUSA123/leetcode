# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:
#
# add(1)
# add(2)
# findMedian() -> 1.5
# add(3)
# findMedian() -> 2

import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return
        if num <= - self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small) - len(self.large) == -2:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        return -float(self.small[0]) if len(self.small) > len(self.large) else float(self.large[0])


mf = MedianFinder()
mf.addNum(1)
print(mf.findMedian())
mf.addNum(2)
print(mf.findMedian())
