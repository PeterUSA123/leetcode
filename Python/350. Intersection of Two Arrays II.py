# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
                del nums2[nums2.index(num)]
        return res


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1_dict = dict()
        result = []
        for n1 in nums1:
            n1_dict[n1] = n1_dict.get(n1, 0) + 1
        for n2 in nums2:
            if n2 in n1_dict and n1_dict.get(n2, 0) > 0:
                result.append(n2)
                n1_dict[n2] -= 1
        return result
