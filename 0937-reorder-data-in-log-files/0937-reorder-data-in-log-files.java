import java.util.*;

class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Deque<String> digits = new ArrayDeque<>();
        List<String> letters = new ArrayList<>();

        for (String log : logs) {
            if (Character.isLetter(log.charAt(log.length()-1))) {
                letters.add(log);
            } else {
                digits.add(log);
            }
        }

        Collections.sort(letters, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String[] o1Split = o1.split(" ", 2);
                String[] o2Split = o2.split(" ", 2);
                
                int compareInt = o1Split[1].compareTo(o2Split[1]);

                if (compareInt == 0) {
                    return o1Split[0].compareTo(o2Split[0]);
                } else {
                    return compareInt;
                }
            }
        });

        while (!digits.isEmpty()) {
            letters.add(digits.removeFirst());
        }
        
        return letters.toArray(new String[letters.size()]);
    }
}