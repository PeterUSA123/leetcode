# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        ch_cnt, num_cnt = 0, 0
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                ch_cnt += 1
                num2 = s.pop()
                num1 = s.pop()
                if tokens[i] == '+':
                    s.append(num1 + num2)
                elif tokens[i] == '-':
                    s.append(num1 - num2)
                elif tokens[i] == '*':
                    s.append(num1 * num2)
                elif tokens[i] == '/':
                    if num1 * num2 < 0:
                        s.append(-(num1 // -num2))
                    else:
                        s.append(num1 // num2)
            else:
                s.append(int(tokens[i]))
                num_cnt += 1
        return s.pop()
