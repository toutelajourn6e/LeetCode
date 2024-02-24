import java.util.*;

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
    public boolean isPalindrome(ListNode head) {
        List<Integer> values = new ArrayList<>();
        ListNode cur = head;

        while (cur != null) {
            values.add(cur.val);
            cur = cur.next;
        }

        int left = 0;
        int right = values.size() - 1;

        while (left < right) {
            if (values.get(left) != values.get(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}