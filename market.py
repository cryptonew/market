import requests,json
import time
requests.packages.urllib3.disable_warnings()


def btc_usd_rate():
    url = "https://bittrex.com/api/v1.1/public/getticker?market=USDT-BTC"
    resp = requests.get(url=url)
    rate = json.loads(resp.text)
    btc_rate = "%.2f" % (float(rate["result"]["Last"]))
    return btc_rate


def btc_usd_sell():
    url = "https://bittrex.com/api/v1.1/public/getorderbook?market=USDT-BTC&type=sell"
    resp = requests.get(url=url)
    sell = json.loads(resp.text)
    return sell


def btc_usd_buy():
    url = "https://bittrex.com/api/v1.1/public/getorderbook?market=USDT-BTC&type=buy"
    resp = requests.get(url=url)
    buy = json.loads(resp.text)
    return buy


def btc_sell_quantity():
    sell_q = 0

    for i in sell.get("result"):
        a = float(i.get("Quantity"))
        sell_q = sell_q +a

    return sell_q


def btc_buy_quantity():
    buy_q = 0

    for i in buy.get("result"):
        a = float(i.get("Quantity"))
        buy_q = buy_q +a

    return buy_q


def print_to():
    print "-------------------------------"
    print "BTC Sell Quantity = " + str(sell_q)
    print "BTC Buy Quantity = " + str(buy_q)
    print "BTC Price = $" + str(btc_rate)
    print ""
    print time.strftime("%Y-%m-%d %H:%M:%S")
    print ""


while True:

    sell = btc_usd_sell()
    sell_q = btc_sell_quantity()

    buy = btc_usd_buy()
    buy_q = btc_buy_quantity()

    btc_rate = btc_usd_rate()

    print_to()
    time.sleep(30)

exit()