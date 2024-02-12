import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagram = new HashMap<>();

        for (String str : strs) {
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String sortedStr = new String(charArr);

            if (!anagram.containsKey(sortedStr)) {
                anagram.put(sortedStr, new ArrayList<>());
            }
            anagram.get(sortedStr).add(str);
        }

        return new ArrayList<>(anagram.values());

    }
}