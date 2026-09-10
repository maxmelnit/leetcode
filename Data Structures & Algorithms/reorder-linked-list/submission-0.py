# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find the middle of linked list with slow + fastx pointer approach
        s = f = head

        # Move slow once/it, and fast twice/it
        while f and f.next:
            s = s.next
            f = f.next.next

        # Now slow = middle of the linked list
        # We need to reverse the second half of the linked list

        # Start of second list is right after the slow pointer
        first = head
        second = s.next
        s.next = None # Break the first list off
        temp = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Set second half back to the start of the new list
        second = prev

        # Now the second list is reversed, and we can alternate them
        res = []
        head = first
        while first and second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second

        while head:
            res.append(head.val)
            head = head.next

        return head





