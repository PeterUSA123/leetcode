# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
#
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        s0 = [0] * len(prices)
        s1 = [0] * len(prices)
        s2 = [0] * len(prices)

        s0[0], s1[0], s2[0] = 0, -prices[0], -2147483648
        # At the start, you don't have any stock if you just rest
        # After buy, you should have -prices[0] profit. Be positive!
        # Lower base case

        for i in range(1, len(prices)):
            # Stay at s0, or rest from s2
            s0[i] = max(s0[i - 1], s2[i - 1])
            # Stay at s1, or buy from s0
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i]);
            # Only one way from s1
            s2[i] = s1[i - 1] + prices[i]

        return max(s0[len(prices) - 1], s2[len(prices) - 1])


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        s0, s1, s2 = 0, -prices[0], 0
        for i in range(1, len(prices)):
            last_s2 = s2
            s2 = s1 + prices[i]
            s1 = max(s0 - prices[i], s1)
            s0 = max(s0, last_s2)

        return max(s0, s2)
