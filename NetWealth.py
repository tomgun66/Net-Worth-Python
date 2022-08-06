
from base64 import urlsafe_b64decode
import profile
from urllib import response
from xmlrpc.client import ResponseError
import requests
import json


def apiCall(url, symbol, object, value, numberOfStocks):
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    responseBody = response.json()
    print(responseBody[symbol])
    x = responseBody[object]
    print(x[value])
    totalValue = float(x[value]) * numberOfStocks
    print(totalValue)
    return totalValue

netWorth = 0.0

urls = ["https://www.vanguardinvestor.co.uk/api/fund-detail/vanguard-ftse-all-world-ucits-etf-usd-distributing", "https://www.vanguardinvestor.co.uk/api/fund-detail/vanguard-ftse-global-all-cap-index-fund-gbp-acc"]
for x in urls:
    try:
        net = apiCall(x, 'ticker', 'marketPrice', 'value', 10)
        netWorth = netWorth + net
    except:
        try:
            net = apiCall(x, 'displayName', 'navPrice', 'value', 10)
            netWorth = netWorth + net
        except:
            print("didn't work")

print(netWorth)