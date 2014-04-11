import json
import urllib

#usd btc price coinbase api
url = "https://coinbase.com/api/v1/prices/spot_rate"
response = urllib.urlopen(url)
data = json.loads(response.read())

current_price = float(data['amount'])

#old price (within an hour)
url = "https://coinbase.com/api/v1/prices/historical"
response = urllib.urlopen(url)
data = response.read()

old_price = float(data[data.find(',')+1:data.find('\n')])

#delta range checks
delta = current_price - old_price

#print "Current " + str(current_price)
#print "Old " + str(old_price)

contents = ""

if delta > 10:
    contents += "BTC rose by 10 USD since last tick!";
elif delta > 25:
    contents += "BTC rose by 25 USD since last tick!";
elif delta > 50:
    contents += "BTC rose by 50 USD since last tick! Sell!";

if delta < -10:
    contents += "BTC fell by 10 USD since last tick!";
elif delta < -25:
    contents += "BTC fell by 25 USD since last tick!";
elif delta < -50:
    contents += "BTC fell by 50 USD since last tick! Buy!";

#notify
if contents:
    import mailer
    mailer.sendmail(contents)
    
    
    

