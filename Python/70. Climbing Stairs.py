# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n

        arr = [0 for i in range(n + 1)]
        arr[1] = 1
        arr[2] = 2
        for i in range(3, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n]


s = Solution()
print(s.climbStairs(3))
