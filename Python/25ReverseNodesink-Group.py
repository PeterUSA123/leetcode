__author__ = 'Minyi'
#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#You may not alter the values in the nodes, only nodes itself may be changed.
#Only constant memory is allowed.
#For example,
#Given this linked list: 1->2->3->4->5
#For k = 2, you should return: 2->1->4->3->5
#For k = 3, you should return: 3->2->1->4->5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        list = []
        tmp = ''
        first = ans = ListNode(0)
        if not head:
            return []
        while head:
            list.append(head.val)
            head = head.next

        for i in range(0,len(list),k):
            if (i+k-1)<len(list):
                tmp = list[i:i+k]
                tmp.reverse()
            else:
                tmp = list[i:]
            for val in tmp:
                    ans.next = ListNode(val)
                    ans = ans.next
        ans.next = None

        return first.next