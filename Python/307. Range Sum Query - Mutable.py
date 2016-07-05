# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.accu = [0]
        self.diff = [0] * len(nums)
        for num in nums:
            self.accu.append(self.accu[-1] + num)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        oval, self.nums[i] = self.nums[i], val
        self.diff[i] += val - oval

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i] + sum(self.diff[i:j + 1])


        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.update(1, 10)
        # numArray.sumRange(1, 2)


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j + 1])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
