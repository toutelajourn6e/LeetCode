# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()
        ans = None
        curA = headA

        while curA:
            nodes.add(curA)
            curA = curA.next

        curB = headB

        while curB:
            if curB in nodes:
                ans = curB
                break
            curB = curB.next

        return ans

