# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        dummy = ListNode()

        while head:
            if head.next is dummy:
                return True

            next_head = head.next
            head.next = dummy
            head = next_head
            
        return False