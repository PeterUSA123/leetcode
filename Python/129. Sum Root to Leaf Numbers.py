# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ans = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.helper(root, "")

    def helper(self, root, num):
        if root == None:
            return None
        num += str(root.val)
        l = self.helper(root.left, num)
        r = self.helper(root.right, num)
        if not l and not r:
            self.ans += int(num)
        return self.ans
