# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        prev, cur, next = None, head, head.next

        while next:
            cur.next = prev
            prev = cur
            cur = next
            next = next.next
        cur.next = prev
        return cur