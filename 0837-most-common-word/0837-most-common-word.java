import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        HashMap<String, Integer> wordCount = new HashMap<>();
        HashSet<String> banSet = new HashSet<>(Arrays.asList(banned));

        String[] pArr = paragraph.replaceAll("\\W+", " ").toLowerCase().split(" ");

        for (String p : pArr) {
            if (!banSet.contains(p)) {
                wordCount.put(p, wordCount.getOrDefault(p, 0) + 1);
            }
        }

        return Collections.max(wordCount.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}