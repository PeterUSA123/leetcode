# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, cursum, valuelist):
            if root.left == None and root.right == None:
                if cursum == sum:
                    ans.append(valuelist)
            if root.left:
                dfs(root.left, cursum + root.left.val, valuelist + [root.left.val])
            if root.right:
                dfs(root.right, cursum + root.right.val, valuelist + [root.right.val])

        ans = []
        if root == None:
            return []
        dfs(root, root.val, [root.val])
        return ans
