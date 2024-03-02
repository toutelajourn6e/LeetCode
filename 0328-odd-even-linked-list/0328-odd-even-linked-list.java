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
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;
        if (head.next == null || head.next.next == null) return head;
        ListNode cur1 = head;
        ListNode cur2 = head.next;
        ListNode init = head.next;

        while (cur1.next != null && cur1.next.next != null) {
            cur1.next = cur1.next.next;
            cur1 = cur1.next;

            if (cur2.next.next != null) {
                cur2.next = cur2.next.next;
                cur2 = cur2.next;
            }
        }
        cur2.next = null;
        cur1.next = init;
        return head;
    }
}