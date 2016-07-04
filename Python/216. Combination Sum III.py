# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Ensure that numbers within the set are sorted in ascending order.
# Example 1:
# Input: k = 3, n = 7
# Output:
# [[1,2,4]]
#
# Example 2:
# Input: k = 3, n = 9
# Output:
# [[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.solution = []
        self.helper(1, k, n, [])
        return self.solution

    def helper(self, start, k, n, result):
        if k == 0 and n == 0:
            self.solution.append(result[:])
        for num in range(start, 10):
            result.append(num)
            if n - num >= 0:
                self.helper(num + 1, k - 1, n - num, result)
            result.pop()
