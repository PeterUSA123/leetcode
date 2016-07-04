# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Note: Do not modify the linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p1 = p2 = head
        flag = False
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                flag = True
                break
        if not flag:
            return None
        while head.next and p1.next:
            if head == p1:
                return head
            head = head.next
            p1 = p1.next