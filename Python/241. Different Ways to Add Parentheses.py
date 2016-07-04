# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
#
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        dic = {}
        return self.getSum(input, dic)

    def getSum(self, string, dic):
        res = []
        sign = False
        if string in dic:
            return dic[string]
        for i in range(len(string)):
            if string[i] in "+-*":
                sign = True
                fore = string[:i]
                after = string[i + 1:]

                foreSums = self.getSum(fore, dic)
                afterSums = self.getSum(after, dic)

                for foreSum in foreSums:
                    for afterSum in afterSums:
                        r = self.cal(foreSum, string[i], afterSum)
                        res.append(r)
                        dic[string] = res
        if not sign:
            return [int(string)]
        return res

    def cal(self, a, sign, b):
        if sign == '+':
            return a + b
        elif sign == '-':
            return a - b
        elif sign == '*':
            return a * b


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return [eval(`a` + c + `b`)
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i + 1:])] or [int(input)]


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return [a + b if c == '+' else a - b if c == '-' else a * b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i + 1:])] or [int(input)]


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n
