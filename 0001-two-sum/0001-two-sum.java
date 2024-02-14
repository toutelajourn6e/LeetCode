import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (numIndex.get(target - nums[i]) == null) {
                numIndex.put(nums[i], i);
            } else {
                return new int[]{numIndex.get(target-nums[i]), i};
            }
        }
        return null;
    }
}