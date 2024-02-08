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
                String[] o1Split = o1.split(" ");
                String[] o2Split = o2.split(" ");

                for (int i = 1; i < Math.min(o1Split.length, o2Split.length); i++) {
                    if (o1Split[i].compareTo(o2Split[i]) >= 1) {
                        return 1;
                    } else if (o1Split[i].compareTo(o2Split[i]) <= -1) {
                        return -1;
                    }
                }

                if (o1Split.length == o2Split.length) {
                    return o1Split[0].compareTo(o2Split[0]);
                } else {
                    return o1Split.length - o2Split.length;
                }
            }
        });

        while (!digits.isEmpty()) {
            letters.add(digits.removeFirst());
        }
        
        return letters.toArray(new String[letters.size()]);
    }
}