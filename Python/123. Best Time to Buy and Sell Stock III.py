# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s1, s2 = 0, 0
        b1, b2 = -2147483648, -2147483648
        for i in range(len(prices)):
            b1 = max(b1, -prices[i])
            s1 = max(s1, b1 + prices[i])
            b2 = max(b2, s1 - prices[i])
            s2 = max(s2, b2 + prices[i])
        return s2
