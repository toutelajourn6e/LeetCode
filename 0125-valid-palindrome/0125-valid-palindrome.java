import java.util.*;

class Solution {
    public boolean isPalindrome(String s) {
        StringBuffer sb = new StringBuffer();

        for (char c : s.toLowerCase().toCharArray()) {
            if (Character.isDigit(c) || Character.isLetter(c)) {
                sb.append(c);
            }
        }

        // System.out.println(sb.toString() + "-----------" + sb.reverse().toString());
        return sb.toString().equals(sb.reverse().toString());
    }
}