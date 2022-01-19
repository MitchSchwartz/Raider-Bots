import os
import requests
from test_mode import testMode, liveOnly
#from time import sleep
#from .bot import Bot
#from bots_online import botList
from update_bot_name import botNameUpdate
#from json import dumps
#from get_server_id import serverList

tokenList = ["RAIDER","AURUM2","GRIMWEED","NEWT"]

def priceInAurum(_tokenPrice, _aurumPrice):

  price = float(_tokenPrice) / float(_aurumPrice)
  return price


def getTokenValues(_test):
  
  auth = os.environ.get("nomicsKey")
  ids = (','.join(tokenList))
  url = f'https://api.nomics.com/v1/currencies/ticker?key={auth}&ids={ids}'
  
    
  
  try:
    r = requests.get(url)
    print(f"\n>>> Nomics response: {r} \n")# {dumps(r.json())}")

  except requests.exceptions.RequestException as e:
    print(f"\n {e}")# "\n", dumps(r.content), "\n")
  


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

  
  if (not liveOnly):
    print("\n>>>Updating Aurum - TEST", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", "test")
  
  if (not testMode):
    print("\n>>> Updating Aurum - CR", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", "cr")

    print("\n>>> Updating Aurum - NFT.IT", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", "nft.it")


  if (not liveOnly):
    print("\n>>> Updating Raider - TEST", "\n")
    botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", "test" )

  if (not testMode):
    print("\n>>> Updating Raider - CR", "\n")
    botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", "cr" )

    print("\n>>> Updating Raider - NFT.IT", "\n")
    botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", "nft.it" )

  
  if (not liveOnly):
    print("\n>>> Updating Grimweed - TEST", "\n")
    botNameUpdate(f"Grmw | {grimweedPrice} AR", "grimweedBot", "test" )

  if (not testMode):
    print("\n>>> Updating Grimweed - CR", "\n")
    botNameUpdate(f"Grmw | {grimweedPrice} AR", "grimweedBot", "cr" )  

    print("\n>>> Updating Grimweed - CR", "\n")
    botNameUpdate(f"Grmw | {grimweedPrice} AR", "grimweedBot", "nft.it" )


  if (not liveOnly):
    print("\n>>>Updating Eye of Newt - TEST", "\n")
    botNameUpdate(f"Newt | {newtPrice} AR", "eyeOfNewtBot", "test")  
  

  if (not testMode):
    print("\n>>> Updating Aurum - CR", "\n")
    botNameUpdate(f"Newt  | {newtPrice} AR", "eyeOfNewtBot", "cr")
    
    print("\n>>> Updating Aurum - NFT.IT", "\n")
    botNameUpdate(f"Newt  | {newtPrice} AR", "eyeOfNewtBot", "nft.it")
  '''
  
  
  #testStatus(grimweedPrice) 
  
  for key in botList:
    if (botlist[key].isToken):
      print(f"\n>>> Updating {botList[key].name} - {key}", "\n")
      botNameUpdate(f"G-WEED | ${botList[key].price}", botList[key].token, "test")  
      print(f"{botList[key].name} - botList[key].price Updated")

  
  
  for x in serverList:
    print(f"\n>>> Updating Grimweed - {x}", "\n")
    botNameUpdate(f"G-WEED | ${grimweedPrice}", "grimweedBot", x)  
    print(f"{x} - grimweed Updated")

  for x in serverList:
    print(f"\n>>> Updating Aurum - {x}", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", aurumBot.token, x)  
    print(f"{x} - Aurumbot Updated")
  '''




  

  
  




