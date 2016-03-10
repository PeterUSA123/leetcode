# Given inorder and postorder traversal of a tree, construct the binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        index = inorder.index(postorder.pop())
        root = TreeNode(inorder[index])

        root.right = self.buildTree(inorder[index + 1:len(inorder)], postorder)
        root.left = self.buildTree(inorder[0:index], postorder)

        return root
