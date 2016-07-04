__author__ = 'Minyi'
#Given a linked list, swap every two adjacent nodes and return its head.
#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.
#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        first = ans = ListNode(0)

        if not head:
            return []
        while head:
            t1 = head
            t2 = head.next

            if t2:
                ans.next = ListNode(t2.val)
                ans.next.next = ListNode(t1.val)
                head = head.next.next
                ans = ans.next.next
            else:
                ans.next = ListNode(t1.val)
                head = head.next
                ans.next.next = None

        return first.next
