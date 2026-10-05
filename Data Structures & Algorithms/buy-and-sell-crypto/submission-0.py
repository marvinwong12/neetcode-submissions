class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_P = 0
        minbuy = prices[0]
        for sell in prices:
            max_P = max(sell - minbuy, max_P)
            minbuy = min(minbuy, sell)
        return max_P

        