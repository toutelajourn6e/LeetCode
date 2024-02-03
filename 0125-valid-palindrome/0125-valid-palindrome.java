class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;

        while (start < end) {
            char s_char = s.charAt(start);
            char e_char = s.charAt(end);
    
            if (!Character.isLetterOrDigit(s_char)) {
                start++;
            } else if (!Character.isLetterOrDigit(e_char)) {
                end--;
            } else if (Character.toLowerCase(s_char) != Character.toLowerCase(e_char)) {
                return false;
            } else {
                start += 1;
                end -= 1;
            }
        }
        return true;
    }
}