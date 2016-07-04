# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a, b = headA, headB
        tmp = ListNode(0)
        t = ListNode(0)
        if headA == headB:
            return headA
        elif headA.next == None:
            while headB.next:
                headB = headB.next
                if headA == headB:
                    return headB
            if headB.next == None:
                return None
        elif headB.next == None:
            while headA.next:
                headA = headA.next
                if headB == headA:
                    return headA
            if headA.next == None:
                return None

        while a.next and b.next:
            if a == b:
                return a
            a = a.next
            b = b.next
        if not a.next:
            tmp = headB
            while b.next:
                tmp = tmp.next
                b = b.next
            t = headA
        else:
            tmp = headA
            while a.next:
                tmp = tmp.next
                a = a.next
            t = headB
        if t == tmp:
            return t
        while t.next and tmp.next:
            t = t.next
            tmp = tmp.next
            if t == tmp:
                return t
        if t.next == None:
            return None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.ne
