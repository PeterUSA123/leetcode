__author__ = 'Minyi'
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n == 0:
            return 0

        merge = []
        while len(nums1)>0 and len(nums2)>0:
            if(nums1[0]<nums2[0]):
                merge.append(nums1[0])
                del nums1[0]
            else:
                merge.append(nums2[0])
                del nums2[0]
        merge.extend(nums1)
        merge.extend(nums2)

        if n%2!=0 :
            return merge[n//2]
        else:
            return (merge[n/2]+merge[n/2-1])/2.0
