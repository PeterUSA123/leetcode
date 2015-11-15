__author__ = 'Minyi'
#Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ans = ListNode(0)
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                tmp = l1.val
                l1 = l1.next
            else:
                tmp = l2.val
                l2 = l2.next
            ans.next = ListNode(tmp)
            ans = ans.next

        if l1:
            ans.next = l1
        if l2:
            ans.next = l2

        return head.next