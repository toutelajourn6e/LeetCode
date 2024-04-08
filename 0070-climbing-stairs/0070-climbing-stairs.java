class Solution {
    static HashMap<Integer, Integer> memo = new HashMap<>();

    public int climbStairs(int n) {
        return climb(n);
    }

    static int climb(int n) {
        if (n <= 1) return 1;
        if (memo.get(n) != null) return memo.get(n);

        memo.put(n, climb(n-1) + climb(n-2));
        return memo.get(n);
    }
}