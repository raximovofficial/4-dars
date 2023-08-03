class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                maxprofit = max(maxprofit,sell - buy)
            else:
                buy = sell
        return maxprofit

a = Solution()
print(a.maxProfit(prices = [7,1,5,3,6,4]))