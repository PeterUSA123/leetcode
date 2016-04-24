# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        curMin = self.getMin()
        if x < curMin or curMin == None:
            curMin = x
        self.array.append((x,curMin))

    def pop(self):
        """
        :rtype: nothing
        """
        self.array.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.array[len(self.array)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.array) == 0:
            return None
        return self.array[len(self.array)-1][1]
