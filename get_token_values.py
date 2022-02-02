import os
import requests
#import discord
#from test_mode import testMode, liveOnly
#from time import sleep
#from .bot import Bot
#from bots_online import botList
from update_bot_name import botNameUpdate
import json 
from get_server_id import serverList

tokenList = ["RAIDER","AURUM2","GRIMWEED","NEWT"]


def priceInAurum(_tokenPrice, _aurumPrice):

  price = float(_tokenPrice) / float(_aurumPrice)
  return price


def getTokenValues():
  
  auth = os.environ.get("nomicsKey")
  ids = (','.join(tokenList))
  url = f'https://api.nomics.com/v1/currencies/ticker?key={auth}&ids={ids}'
  
    
  
  try:
    r = requests.get(url)
    print(f"\n>>> Nomics response: {r} \n")# {dumps(r.json())}")

  except requests.exceptions.RequestException as e:
    print(f"\n {e}")# "\n", dumps(r.content), "\n")
  
  nomicsResults = r.json()

  print(f"\n>>>Nomics Results: {json.dumps(nomicsResults)}")

  

  i=0

  while i < len(tokenList):  
    if r.json()[i]['currency'] == "AURUM2":
      aP = r.json()[i]['price']

      print("\n", ">>> aP:", aP, "\n")

    if r.json()[i]['currency'] == "RAIDER":
      rP = r.json()[i]['price']

      print("\n", ">>> rP:", rP, "\n")
    
    if r.json()[i]['currency'] == "GRIMWEED":
      gP = r.json()[i]['price']

       
    if r.json()[i]['currency'] == "NEWT":
      nP = r.json()[i]['price']

     # print("\n", ">>> gP:", gP, "\n")

    i += 1


  
  aurumPrice = "{:10.4f}".format(float(aP))

  raiderPrice = "{:10.2f}".format(float(rP))
  
  gPaP = priceInAurum(gP, aurumPrice)
  grimweedPrice = "{:10.2f}".format(float(gPaP))


  nPaP = priceInAurum(nP, aurumPrice)
  newtPrice = "{:10.2f}".format(float(nPaP))

  
  #print(f"\n>>> Aurum: {aurumPrice} | Raider: {raiderPrice} | Grimweed: {grimweedPrice}")# | Newt: {newtPrice} \n")

  
  _serverList = serverList

  if (testMode):
    _serverList = ["test"]   
  
  for x in _serverList:    

  
    print(f"\n>>> Updating Aurum - {x}", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", x)  
    print(f"{x} - Aurumbot Updated")
    
    print("\n>>> Updating Raider - {x}", "\n")
    botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", x )
    print(f"{x} - RaiderBot Updated")

    print(f"\n>>> Updating Grimweed - {x}", "\n")
    botNameUpdate(f"G-WEED | ${grimweedPrice}", "grimweedBot", x)  
    print(f"{x} - Grimweed Updated")

    print("\n>>> Updating Eye of Newt - {x}", "\n")
    botNameUpdate(f"Newt  | {newtPrice} AUR", "eyeOfNewtBot", x)
    print(f"{x} - Newt Updated")


  




  

  
  




