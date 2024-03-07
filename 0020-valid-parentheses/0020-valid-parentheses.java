import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        List<Character> close = new ArrayList(Arrays.asList(')', '}', ']'));

        for (char c : s.toCharArray()) {
            if (close.contains(c) && !stack.isEmpty()) {
                if (c == ')' && stack.peek() == '(') {
                    stack.pop();
                } else if (c == '}' && stack.peek() == '{') {
                    stack.pop();
                } else if (c == ']' && stack.peek() == '[') {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        if (stack.isEmpty()) return true;
        else return false;
    }
}