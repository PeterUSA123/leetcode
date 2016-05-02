# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        s = []
        for num in nums:
            s.append(str(num))
        s.sort(cmp=lambda x, y: cmp(int(y + x), int(x + y)))
        ans = ''.join(s)
        idx = 0
        for ch in ans:
            if ch == '0':
                idx += 1
            else:
                break
        if idx == len(ans):
            return ans[idx - 1]
        else:
            return ans[idx:]
