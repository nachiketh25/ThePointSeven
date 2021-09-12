import requests
currency = input("Enter currency name : ")
url =  'https://api.coinbase.com/v2/exchange-rates?currency='+currency
response = requests.get(url)
data = response.json()

usd = data['data']['rates']['USD']
eth = data['data']['rates']['ETH']
btc = data['data']['rates']['BTC']
doge = data['data']['rates']['DOGE']
print("*****************************************************************")
print("The current exchange value of the above crypto is as below")
print("*****************************************************************")
print("USD :", usd)
print("ETH :",eth)
print("BTC :",btc)
print("DOGE :",doge)