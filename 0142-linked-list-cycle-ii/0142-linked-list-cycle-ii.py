# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = hare = head

        while tortoise != None and hare != None:
            if hare.next is None:
                return None
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare:
                break
        else: return None

        hare = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        return hare
