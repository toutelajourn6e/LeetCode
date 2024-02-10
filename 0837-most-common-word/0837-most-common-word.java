import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        HashMap<String, Integer> wordCount = new HashMap<>();
        HashSet<String> banSet = new HashSet<>();
        for (String ban : banned) {
            banSet.add(ban.toLowerCase());
        }


        paragraph = paragraph.replaceAll("[!?',;.]", " ");
        String[] pList = paragraph.split(" ");

        for (String p : pList) {
            p = p.toLowerCase();

            if (!banSet.contains(p) && !p.equals("")) {
                if (wordCount.get(p) == null) {
                    wordCount.put(p, 1);
                } else {
                    wordCount.put(p, wordCount.get(p) + 1);
                }
            }
        }

        List<Map.Entry<String, Integer>> entryList = new ArrayList<>(wordCount.entrySet());
        entryList.sort((o1, o2) -> {
            return o2.getValue() - o1.getValue();
        });

        return entryList.get(0).getKey();
    }
}