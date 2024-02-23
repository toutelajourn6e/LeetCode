class Solution {
    public int maxProfit(int[] prices) {
        int profit  = 0;
        int buy = Integer.MAX_VALUE;

        for (int price : prices) {
            if (profit < (price - buy)) {
                profit = price - buy;
            }
            
            if (price < buy) {
                buy = price;
            }
        }

        return profit;
    }
}