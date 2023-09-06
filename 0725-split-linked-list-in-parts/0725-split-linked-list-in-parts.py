# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        ret_list = []
        q, r = divmod(length, k)
        cnt = [q] * k
        for i in range(r):
            cnt[i] += 1
        
        for c in cnt:
            cur = head
            ret_list.append(head)
            for _ in range(c-1):
                cur = cur.next
            else:
                if cur is not None:
                    head = cur.next
                    cur.next = None

        return ret_list