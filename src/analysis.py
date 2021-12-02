from stock import Stock
from market import Market
from account import Account
from helpers import print_json


if __name__ == "__main__":

    #individual tickers
    apple = Stock(symbol="AAPL")

    #symbols can be either $SPX.X, $DJI, or $COMPX
    spx = Market(symbol="$SPX.X")

    #todo
    keith = Account()

    res = apple.get_price_history(period=1, periodType='day', frequencyType='minute')

    #real time quote
    quote = apple.get_quote()
    spx_movers = spx.get_movers(symbol='$SPX.X', direction='up', change='percent')
    print_json(quote)

    