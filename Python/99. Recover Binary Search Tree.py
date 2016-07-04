# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val

    def __init__(self):
        self.n1 = None
        self.n2 = None
        self.pre = None

    def inorder(self, root):
        if not root:
            return root

        self.inorder(root.left)
        if not self.pre:
            self.pre = root
        else:
            if not self.n1 and root.val < self.pre.val:
                self.n1 = self.pre
            if self.n1 and root.val < self.pre.val:
                self.n2 = root
            else:
                self.pre = root
        self.inorder(root.right)
