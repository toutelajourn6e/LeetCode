import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, Integer> anagram = new HashMap<>();
        List<List<String>> result = new ArrayList<>();
        int size = 0;

        for (String str : strs) {
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String sortedStr = new String(charArr);

            if (anagram.get(sortedStr) == null) {
                result.add(new ArrayList<String>());
                result.get(size).add(str);
                anagram.put(sortedStr, size);
                size++;
            } else {
                result.get(anagram.get(sortedStr)).add(str);
            }
        }

        return result;

    }
}