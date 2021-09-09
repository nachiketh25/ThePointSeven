import requests
import json
x = requests.get('https://api.imgflip.com/get_memes')
print(x)
print(x.json())