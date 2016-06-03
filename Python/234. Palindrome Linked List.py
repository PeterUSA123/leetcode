# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)

        while stack:
            if stack.pop() != head.val:
                return False
            head = head.next

        return True


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = []
        while head:
            s += head.val,
            head = head.next
        return s == s[::-1]
