"""
1475. Final Prices With a Special Discount in a Shop

You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.
"""


# Monotonic stack solution  O(n)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = []
        result_prices = prices.copy()

        for i, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                discount_index = stack.pop()
                result_prices[discount_index] -= price

            stack.append(i)

        return result_prices


# Not using enumerate
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = []
        result_prices = prices.copy()

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                discount_index = stack.pop()
                result_prices[discount_index] -= prices[i]

            stack.append(i)

        return result_prices


# Brute force O(n^2) solution
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        discount_prices = prices.copy()

        for i in range(len(prices)):

            for k in range(i + 1, len(prices)):
                if prices[k] <= prices[i]:
                    discount_prices[i] = prices[i] - prices[k]
                    break

        return discount_prices
