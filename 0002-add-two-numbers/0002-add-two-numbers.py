# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry, sum = divmod(sum, 10)
            cur.next = ListNode(sum)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        cur2 = l1 or l2

        while cur2:
            sum = cur2.val + carry
            carry, sum = divmod(sum, 10)
            cur.next = ListNode(sum)
            cur = cur.next
            cur2 = cur2.next

        if carry: cur.next = ListNode(1)

        return head.next