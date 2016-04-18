# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        valuelist = []
        p = head
        valuelist.append(p)
        while p.next:
            p = p.next
            valuelist.append(p)
        if len(valuelist) <= 2:
            return
        n = len(valuelist)
        rlist = valuelist[::-1]
        res = ListNode(0)

        for i in range(n/2):
            valuelist[i].next = rlist[i]
            rlist[i].next = valuelist[i+1]
        if n%2 == 0:
            rlist[n/2-1].next = None
        else:
            rlist[n/2].next = None