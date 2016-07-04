# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        else:
            root.next = None
            self.help(root)

    def help(self, node):
        if node.left:
            if node.right:
                node.left.next = node.right
            else:
                node.left.next = None
            self.help(node.left)
        if node.right:
            if node.next and node.next.left:
                node.right.next = node.next.left
            else:
                node.right.next = None
            self.help(node.right)
