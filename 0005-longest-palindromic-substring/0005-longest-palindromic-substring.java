class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int[] answer = {0, 1};
        
        for (int i = 0; i < n; i++) {
            int start = i, end = i;
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

            start = i;
            end = i + 1;
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
        return s.substring(answer[0], answer[1]);
    }
}