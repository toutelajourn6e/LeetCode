/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null) return null;
        if (head.next == null) return head;

        ListNode prev = new ListNode(0), cur = head, next = null, nNext = null;
        ListNode answer = head.next;

        while (cur != null && cur.next != null) {
            next = cur.next;
            nNext = next.next;
            prev.next = next;

            next.next = cur;
            cur.next = nNext;

            prev = cur;
            cur = cur.next;
        }

        return answer;
    }
}