__author__ = 'Minyi'
import heapq
#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heaplist = []
        head = ans = ListNode(0)

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heaplist,(lists[i].val,i))

        while heaplist:
            value,index = heapq.heappop(heaplist)
            ans.next = lists[index]
            lists[index] = lists[index].next
            ans = ans.next
            if lists[index]:
                heapq.heappush(heaplist,(lists[index].val,index))

        ans.next = None
        return  head.next


