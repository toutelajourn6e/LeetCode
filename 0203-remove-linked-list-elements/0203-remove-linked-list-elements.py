# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      if head is None: return None
      cur = pre = ListNode(0, head)
      next = cur.next

      while next:
        if next.val == val:
          while next and next.val == val:
            next = next.next
          else:
            cur.next = next
        else:
          next = next.next
          cur = cur.next

      return pre.next