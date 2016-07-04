# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        x = head.val
        h1 = ListNode(None)
        c1 = h1
        h2 = ListNode(None)
        c2 = h2
        h3 = ListNode(None)
        c3 = h3

        c = head
        while c != None:
            n = c.next
            if c.val < x:
                c1.next = c
                c1 = c1.next
            elif c.val > x:
                c2.next = c
                c2 = c2.next
            else:
                c3.next = c
                c3 = c3.next
            c.next = None
            c = n
        sorted_h1 = self.sortList(h1.next)
        sorted_h2 = self.sortList(h2.next)

        if sorted_h1 == None:
            c3.next = sorted_h2
            return h3.next

        tail_h1 = sorted_h1
        while tail_h1.next != None:
            tail_h1 = tail_h1.next
        tail_h1.next = h3.next
        c3.next = sorted_h2
        return sorted_h1
