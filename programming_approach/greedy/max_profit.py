from algo_fermat_utils.helpers import measure_performance


@measure_performance
def maximum_profit(prices):
    """
    Given a list of prices, find the maximum profit that can be made by buying and selling a stock.
    :param prices: list of prices
    :return: the maximum profit
    """
    max_profit = 0
    min_price = float("inf")
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


if __name__ == "__main__":
    print(maximum_profit([7, 1, 5, 3, 6, 4]))  # 5 because buy at 1 and sell at 6
    print(maximum_profit([7, 6, 4, 3, 1]))  # 0 because the price is always decreasing
