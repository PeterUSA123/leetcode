# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        ans = ListNode(0)
        ans.next = head
        pre = ans.next
        cur = ans.next

        while cur:
            if pre.val != cur.val:
                pre.next = cur
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return ans.next