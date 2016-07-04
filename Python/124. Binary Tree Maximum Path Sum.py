# Given a binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    current_max = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dp(root)
        return self.current_max

    def dp(self, root):
        if root == None:
            return 0
        left = self.dp(root.left)
        right = self.dp(root.right)

        if not left or left < 0:
            left = 0
        if not right or right < 0:
            right = 0
        self.current_max = max(left + right + root.val, self.current_max)
        return max(left, right) + root.val
