# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if not num in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        arr1 = sorted(dic.iteritems(), key=lambda d: d[1], reverse=True)
        res = []
        for idx in range(len(arr1)):
            res.append(arr1[idx][0])
        return res[:k]


import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # mc = collections.Counter(nums).most_common(k)
        # return list(map(lambda x: x[0], mc))
        c = collections.Counter(nums)
        return [x[0] for x in c.most_common(k)]


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mc = collections.Counter(nums).most_common(k)
        return list(map(lambda x: x[0], mc))
        # c = collections.Counter(nums)
        # return [x[0] for x in c.most_common(k)]
