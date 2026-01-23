"""
🚀 121. Best Time to Buy and Sell Stock

🤖 Question : You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
⚠️ Difficulty : 🟩Easy
🧩 Topics : Array, Dynamic Programming
🏢 Companies : Amazon, Microsoft

🔮 Algorithm : Single Pass 

1. Take variables min_price and max_profit to keep track of minimum price and maximum profit in the array.
2. Start a loop for each element in prices.
3. Take a temporary variable to calculate profit for each element in the array.
4. Update min_price if found smaller element than min_price.
5. Same with max_profit, update it if found bigger profit.
6. After loop ends, return max_profit.

💎 Time Complexity : O(n)
💎 Space Complexity : O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> float:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            profit = price - min_price
            if price < min_price:
                min_price = price
            elif profit > max_profit:
                max_profit = profit

        return max_profit


# main code
if __name__ == "__main__":
    stock1 = [7, 1, 5, 3, 6, 4]
    stock2 = [0, 7, 4, 3, 4, 5, 3, 2, 1, 9]

    sol = Solution()
    print("Max profit for stock1:", sol.maxProfit(stock1))
    print("Max profit for stock2:", sol.maxProfit(stock2))