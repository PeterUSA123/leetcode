# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.res = []
        path = []
        if root == None:
            return []
        self.dfs(path, root)
        return self.res

    def dfs(self, path, node):
        path.append(str(node.val))
        if node.left == None and node.right == None:
            self.res.append("->".join(path))
        if node.left:
            self.dfs(path, node.left)
        if node.right:
            self.dfs(path, node.right)
        path.pop()