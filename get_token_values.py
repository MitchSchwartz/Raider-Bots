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

tokenList = ["RAIDER","AURUM2","GRIMWEED","NEWT","MHP2"]


# ###tokenlist constructor
# def getTokenList():
#   #print (f"\n>>>{botList}")  
#   tokenList = []
  
#   for x in botList:

#     symbol = botList[x].symbol
#     if (symbol):
#        tokenList.append(botList[x].symbol)
  
#   print (f"\n>>>{tokenList}")  
#   return tokenList
  

def priceInAurum(_tokenPrice, _aurumPrice):

  price = float(_tokenPrice) / float(_aurumPrice)
  return price


def getTokenValues():
  
  perPage = tokenList.__len__
  auth = os.environ.get("nomicsKey")
  ids = (','.join(tokenList))
  url = f'https://api.nomics.com/v1/currencies/ticker?key={auth}&per-page={perPage}&ids={ids}'
  
    
  
  try:
    r = requests.get(url)
    print(f"\n>>> Nomics response: {r} \n")# {dumps(r.json())}")

  except requests.exceptions.RequestException as e:
    print(f"\n {e}")# "\n", dumps(r.content), "\n")
  
  #nomicsResults = r.json()

  #print(f"\n>>>Nomics Results: {json.dumps(nomicsResults)}")

  #print(len(json.loads(r.text)))

  try:
  
    i=0
  
      
    while i < len(json.loads(r.text)): 
       
      if r.json()[i]['currency'] == "AURUM2":
        aP = r.json()[i]['price']
  
  
      if r.json()[i]['currency'] == "RAIDER":
        rP = r.json()[i]['price']
  
      
      if r.json()[i]['currency'] == "GRIMWEED":
        gP = r.json()[i]['price']
  
         
      if r.json()[i]['currency'] == "NEWT":
        nP = r.json()[i]['price']
  
      if r.json()[i]['currency'] == "MHP2":
        mP = r.json()[i]['price']
  
     
      i += 1
  
  except:
    print(f"\n Error processing nomics response")
    return("Token bot updates skipped")
  
  
  aurumPrice = "{:10.4f}".format(float(aP))

  raiderPrice = "{:10.2f}".format(float(rP))
  
  gPaP = priceInAurum(gP, aurumPrice)
  grimweedPrice = "{:10.2f}".format(float(gPaP))


  nPaP = priceInAurum(nP, aurumPrice)
  newtPrice = "{:10.2f}".format(float(nPaP))

  mPaP = priceInAurum(mP, aurumPrice)
  mhpPrice = "{:10.2f}".format(float(mPaP))

  
  print(f"\n>>> Aurum: {aurumPrice} | Raider: {raiderPrice} | Grimweed: {grimweedPrice}")# | Newt: {newtPrice} \n")

  
  _serverList = serverList

  if (testMode):
    _serverList = ["test"]   
  
  print(f"\n>>>testMode: {testMode}")

    
  #print(f"\n>>>serverList: {_serverList}")

  for x in _serverList:    
    print(f"\n>>>x: {x}")
  
    #print(f"\n>>> Updating Aurum - {x}", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", x)  
    #print(f"{x} - Aurumbot Updated")
    
    #print(f"\n>>> Updating Raider - {x}", "\n")
    botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", x )
    #print(f"{x} - RaiderBot Updated")

   #print(f"\n>>> Updating Grimweed - {x}", "\n")
    botNameUpdate(f"Grmw | {grimweedPrice} AUR", "grimweedBot", x)  
    #print(f"{x} - Grimweed Updated")

    #print(f"\n>>> Updating Eye of Newt - {x}", "\n")
    botNameUpdate(f"Newt  | {newtPrice} AUR", "eyeOfNewtBot", x)
    #print(f"{x} - Newt Updated")
    
    #print(f"\n>>> Updating MHP - {x}", "\n")
    botNameUpdate(f"MHP  | {mhpPrice} AUR", "mhpBot", x)
    #print(f"{x} - MHP Updated")

  
  




  

  
  




