# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = hare = head
        while tortoise != None and hare != None:
            if hare.next is None:
                return False
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False
