import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        Arrays.sort(nums);

        
        for (int i = 0; i < nums.length; i++) {
            int firstSelected = nums[i];
            int left = i, right = nums.length - 1;

            while (left < right) {
                if (left == i) left++;
                if (right == i) right--;
                if (left == right || right >= nums.length) break;

                if (firstSelected + nums[left] + nums[right] == 0) {
                    List<Integer> arr = new ArrayList<>(Arrays.asList(firstSelected, nums[left], nums[right]));
                    Collections.sort(arr);
                    result.add(arr);
                    left++;
                } else if (firstSelected + nums[left] + nums[right] < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        List<List<Integer>> answer = new ArrayList<>(result);
        return answer;
    }
}