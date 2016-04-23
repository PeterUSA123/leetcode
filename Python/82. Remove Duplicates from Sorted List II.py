#Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

#For example,
#Given 1->2->3->3->4->4->5, return 1->2->5.
#Given 1->1->1->2->3, return 2->3.

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
		
		pre = ans
		cur = ans.next
		
		while cur != None:
			while cur.next and cur.next.val == pre.next.val:
			    cur = cur.next
			if pre.next == cur:
			    pre = pre.next
			else:
			    pre.next = cur.next
			cur = cur.next
		return ans.next
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = ans = ListNode(0)
        p.next = head
        flag = False
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
                flag = True
            if flag:
                p.next = head.next
                head = head.next
                flag = False
            else:
                p = p.next
                head = head.next
        return ans.next
