# Count the number of prime numbers less than a non-negative number, n.

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        isPrime = [1] * n
        isPrime[0] = 0
        isPrime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(2, (n - 1) / i + 1):
                    isPrime[i * j] = 0
        return sum(isPrime)


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        isPrime = [1] * n
        isPrime[0] = 0
        isPrime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * len(isPrime[i * i:n:i])
        return sum(isPrime)
