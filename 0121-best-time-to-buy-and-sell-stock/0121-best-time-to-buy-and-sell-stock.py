class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = [0]
        buy, sell = 100000, -1

        for price in prices:
            if price < buy:
                if sell >= 0:
                    ans.append(sell - buy)
                    sell = -1
                buy = price
                continue
            if price > sell:
                sell = price

        ans.append(sell - buy)

        return max(ans)
                

