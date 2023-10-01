# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        
        n = len(result)
        if n % 2:
            l1, l2 = result[:n//2], result[(n//2)+1:]
            return l1 == l2[::-1]
        else:
            l1, l2 = result[:n//2], result[n//2:]
            return l1 == l2[::-1]