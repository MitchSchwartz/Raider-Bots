from lib2to3.pgen2 import token
import os
import requests
#import discord
from test_mode import testMode
#from time import sleep
#from .bot import Bot
#from bots_online import botList
from update_bot_name import botNameUpdate
import json
from get_server_id import serverList

tokenList = ["RAIDER", "AURUM2", "GRIMWEED", "NEWT", "MHP2"]
tokenInAurum = ["GRIMWEED","NEWT","MHP2"]

def priceInAurum(_tokenPrice, _aurumPrice):
  price = float(_tokenPrice) / float(_aurumPrice)
  return price

def getTokenValues():
  perPage = len(tokenList)
  auth = os.environ.get("nomicsKey")
  ids = (','.join(tokenList))
  url = f'https://api.nomics.com/v1/currencies/ticker?key={auth}&per-page={perPage}&ids={ids}'

  try:
    r = requests.get(url)
    print(f"\n>>> Nomics response: {r} \n")  # {dumps(r.json())}")

  except requests.exceptions.RequestException as e:
    print(f"\n {e}")  # "\n", dumps(r.content), "\n")

  tokenPrices = {}

  try:
    i = 0

    while i < len(json.loads(r.text)):
      
      if r.json()[i]['currency'] in tokenList:
        tokenName = r.json()[i]['currency']
        tokenPrices[tokenName] = { 
          "price": "{:10.2f}".format(float(r.json()[i]['price']))          
        }

      i += 1
      
  except:
    print(f"\n Error processing nomics response")
    return ("Token bot updates skipped")

  for tIA in tokenInAurum:
    tokenPrices[tIA]["price"] = "{:10.2f}".format(float(priceInAurum(tokenPrices[tIA]["price"], tokenPrices["AURUM2"]["price"])))

  for tokenName in tokenList:
    print(f"Token Price: {tokenName}: {tokenPrices[tokenName]['price']}")

  return tokenPrices
