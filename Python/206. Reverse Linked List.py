# Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        stack = []
        while head:
            stack.append(head)
            head = head.next

        head = stack.pop()
        p = head
        while stack:
            p.next = stack.pop()
            p = p.next
        p.next = None
        return head
