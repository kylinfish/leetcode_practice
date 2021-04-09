# coding=UTF-8
"""
找尋最大的獲利，最好的作法是累加所有賺得到的區段獲利就是最大獲利
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1 or len(prices) >= 3 * pow(10, 4):
            return 0

        buy_price = prices[0]
        profit = diff = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[i-1]:
                diff = prices[i] - buy_price
                if i == len(prices) - 1:
                    profit += diff
                    diff = 0
            else:
                profit += diff
                diff = 0
                buy_price = prices[i]

        return profit


class Solution2():
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1 or len(prices) >= 3 * pow(10, 4):
            return 0

        max_profits = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                max_profits += prices[i] - prices[i-1]

        return max_profits


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3, 2, 6, 5, 0, 3]))
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
