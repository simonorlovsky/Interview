def get_max_profit(stock_prices):
    max_profit = -100000
    # go over each stock price
    for i in range(len(stock_prices)):
        # go over each stock price after i
        for j in range(len(stock_prices)-i):
            if stock_prices[i+j] - stock_prices[i] > max_profit:
                max_profit = stock_prices[i+j] - stock_prices[i]
                print("New: %d, Old: %d" % (stock_prices[i+j],stock_prices[i]))
    return max_profit

def main():
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    print get_max_profit(stock_prices_yesterday)
    # returns 6 (buying for $5 and selling for $11)

main()
