# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, array):
        l = len(array)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(array[0])
        root = TreeNode(array[l // 2])
        root.left = self.sortedArrayToBST(array[:l // 2])
        root.right = self.sortedArrayToBST(array[l // 2 + 1:])
        return root

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        tmp = head
        while tmp:
            array.append(tmp.val)
            tmp = tmp.next

        return self.sortedArrayToBST(array)