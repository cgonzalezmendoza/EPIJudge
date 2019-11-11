from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    max_val, min_val = prices[0], prices[0]
    max_diff = 0
    for val in prices[1:]:
        if val >= max_val:
            max_val = val
            curr_diff = max_val - min_val
            max_diff = max_diff if curr_diff < max_diff else curr_diff
        else:
            max_val = val
            min_val = val if val < min_val else min_val
    return max_diff


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
