# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k == 0 or head == None:
            return head

        node = ListNode(0)
        node.next = head

        t = node
        size = 0
        while t.next:
            t = t.next
            size += 1

        t.next = node.next

        for i in range(size - (k % size)):
            t = t.next
        head = t.next
        t.next = None
        return head
