def calculate_price_index(prices):
    total_value = sum(price.value for price in prices)
    num_prices = len(prices)
    if num_prices > 0:
        price_index = total_value / num_prices
    else:
        price_index = 0
    return price_index

