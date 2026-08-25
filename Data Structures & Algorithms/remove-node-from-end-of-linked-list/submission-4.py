# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        slow = head
        fast = head
        slow_prev = head

        # Place the fast pointer n steps ahead of the slow pointer
        for i in range(n):
            fast = fast.next

        while fast:
            slow_prev = slow
            slow = slow.next
            fast = fast.next


        # If we're removing the head
        if slow_prev == slow:
            return head.next

        slow_prev.next = slow.next
        return head