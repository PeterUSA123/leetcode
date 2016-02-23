# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tmp = head

        before = None
        for i in range(1, m):
            before = tmp
            tmp = tmp.next

        # beforeM is the (m-1)th one in list before reverse, atM is the (m)th one.
        posM = tmp

        # reverse link from m to n
        pre = tmp
        tmp = tmp.next
        for i in range(m + 1, n + 1):
            t = tmp.next
            tmp.next = pre
            pre = tmp
            tmp = t

        posM.next = tmp
        # end of the sublist
        if before:
            before.next = pre
        # in case m == 1, i.e no one before m
        else:
            head = pre

        return head
