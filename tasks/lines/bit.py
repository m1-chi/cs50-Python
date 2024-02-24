import json
import requests
import sys


try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        sys.argv[1] = float(sys.argv[1])
        price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = price.json()
        dollarprice = o["bpi"]["USD"]["rate_float"]
        dollarprice = dollarprice * sys.argv[1]
        print(f"${dollarprice:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit()
# Hello