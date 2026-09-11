# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from collections import defaultdict
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        # Use a heap
        heap = []

        # Counter used to break ties without triggering TypeError
        counter = 0

        for l in lists:
            head = l
            while head:

                heapq.heappush(heap, (head.val, counter, head)) # Tuple is hashable
                counter += 1
                head = head.next

        dummy = ListNode()
        curr = dummy
        while heap:
            curr.next = ListNode(heapq.heappop(heap)[0])
            curr = curr.next

        return dummy.next




