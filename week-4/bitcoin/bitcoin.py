import requests
import sys


try:
    # Convert command-line argument to a float
    btc_amount = float(sys.argv[1])
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    btc_current_price = r["bpi"]["USD"]["rate_float"]
    btc_value = btc_amount * btc_current_price
except requests.RequestException:
    ...
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
else:
    print(f"${btc_value:,.4f}")
