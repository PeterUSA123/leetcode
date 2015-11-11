__author__ = 'minyi'


# Given a linked list, remove the nth node from the end of list and return its head.
# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        cpy = ListNode(0)
        cpy.next = head
        p = cpy
        q = cpy

        for i in range(n):
            p = p.next

        while p.next != None:
            p = p.next
            q = q.next

        tmp = q.next
        q.next = tmp.next
        del tmp

        return cpy.next
