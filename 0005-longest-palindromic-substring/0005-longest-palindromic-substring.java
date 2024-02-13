class Solution {
    int[] answer = {0, 1};

    public String longestPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            find(i ,i, s);
            find(i, i + 1, s);
        }
        return s.substring(answer[0], answer[1]);
    }

    public void find(int start, int end, String s) {
        int n = s.length();
        while (start >= 0 && end < n) {
            if (s.charAt(start) == s.charAt(end)) {
                if ((answer[1] - answer[0]) < ((end+1) - start)) {
                    answer[1] = end + 1;
                    answer[0] = start;
                }
                start--;
                end++;
            } else {
                break;
            }
        }
    }
}