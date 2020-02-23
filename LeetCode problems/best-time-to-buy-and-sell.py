# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 121. Best Time to Buy and Sell Stock

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.


# sol 1: Brute Force

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = []
        max_profit = 0
        if len(prices)==0 or len(prices)==1:
            return 0
        for i in range(len(prices)-1):
            buy = prices[i]
            sell = max(prices[i+1:])
            profit = sell - buy
            if profit>max_profit:
                max_profit = profit
        return max_profit


 # sol 2: better than 1st solution. Single pass

 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif((prices[i] - min_price) > max_profit):
                max_profit  = prices[i] - min_price
        return max_profit   