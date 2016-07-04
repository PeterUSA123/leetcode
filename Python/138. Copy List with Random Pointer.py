# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return

        # copy nodes
        cur = head
        while cur:
            nextNode = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = nextNode
            cur = nextNode

        # copy random pointer
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # separate two parts
        ans = cur = head.next
        while cur.next:
            head.next = cur.next
            head = head.next
            cur.next = head.next
            cur = cur.next
        head.next = None
        return ans


# use dictionary
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        cur = head
        nodedict = {}

        # copy nodes
        while cur:
            nodedict[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head

        # copy random pointers
        while cur:
            if cur.random:
                nodedict[cur].random = nodedict[cur.random]
            if cur.next:
                nodedict[cur].next = nodedict[cur.next]
            cur = cur.next
        return nodedict[head]
