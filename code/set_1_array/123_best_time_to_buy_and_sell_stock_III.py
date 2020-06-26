# Best Time to Buy and Sell Stock III
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit.
# You may complete at most two transactions.
# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# Example 2:
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# ========================================================================
# Algorithm:
# TC: O(n)
# SC: O(n)


def max_profit(prices):

    if not prices:
        return 0

    max_total_profit = 0
    min_price_so_far = prices[0]
    first_transaction_profits = [0] * len(prices)

    # Forward phase: for each day, record maximum profit if sell on that day
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_transaction_profits[i] = max_total_profit

    # Backward phase: for each day, calculate maximum profit
    # if make second transaction on that day
    max_price_so_far = prices[-1]
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price + first_transaction_profits[i-1])
        first_transaction_profits[i] = max_total_profit
    return max_total_profit


if __name__ == "__main__":

    # nums = [3, 3, 5, 0, 0, 3, 1, 4]    # output: 6
    # nums = [1, 2, 3, 4, 5]   # output: 4
    nums = [7, 6, 4, 3, 1]   # output: 0
    print(max_profit(nums))
