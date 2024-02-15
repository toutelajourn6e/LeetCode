class Solution {
    public int trap(int[] height) {
        int result = 0, store = 0, wallHeight = 0, wallIndex = 0;

        for (int i = 0; i < height.length; i++) {
            if (height[i] >= wallHeight) {
                wallHeight = height[i];
                wallIndex = i;
                result += store;
                store = 0;
            } else {
                store += (wallHeight - height[i]);
            }
            System.out.println("store-----" + store);
            System.out.println("result-----" + result);
        }

        if (store > 0) {
            store = wallHeight = 0;
            for (int i = height.length-1; i >= wallIndex; i--) {
                if (height[i] >= wallHeight) {
                wallHeight = height[i];
                result += store;
                store = 0;
            } else {
                store += (wallHeight - height[i]);
            }
            System.out.println("store-----" + store);
            System.out.println("result-----" + result);
            }
        }
        return result;
    }
}
