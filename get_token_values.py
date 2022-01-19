import os
import requests
#from time import sleep
#from .bot import Bot
#from bots_online import botList
from update_bot_name import botNameUpdate
#from json import dumps
#from get_server_id import serverList

tokenList = ["RAIDER","AURUM2","GRIMWEED","NEWT"]

def priceInAurum(_tokenPrice, _aurumPrice):
  int(float(_tokenPrice))
  int(float(_aurumPrice))
  _tokenPrice /= _aurumPrice
  return _tokenPrice

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
  
  #gP = priceInAurum(gP, aurumPrice)
  grimweedPrice = "{:10.2f}".format(float(gP))

  newtPrice = "{:10.2f}".format(float(nP))

  
  #print(f"\n>>> Aurum: {aurumPrice} | Raider: {raiderPrice} | Grimweed: {grimweedPrice}")# | Newt: {newtPrice} \n")

  
  
  print("\n>>>Updating Aurum - TEST", "\n")
  botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", "test")
  
  if (not _test):
    print("\n>>> Updating Aurum - CR", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", "cr")

    print("\n>>> Updating Aurum - NFT.IT", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", "nft.it")



  print("\n>>> Updating Raider - TEST", "\n")
  botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", "test" )

  if (not _test):
    print("\n>>> Updating Raider - CR", "\n")
    botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", "cr" )

    print("\n>>> Updating Raider - NFT.IT", "\n")
    botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", "nft.it" )

  

  print("\n>>> Updating Grimweed - TEST", "\n")
  botNameUpdate(f"Grmw | ${grimweedPrice}", "grimweedBot", "test" )

  if (not _test):
    print("\n>>> Updating Grimweed - CR", "\n")
    botNameUpdate(f"Grmw | ${grimweedPrice}", "grimweedBot", "cr" )  

    print("\n>>> Updating Grimweed - CR", "\n")
    botNameUpdate(f"Grmw | ${grimweedPrice}", "grimweedBot", "nft.it" )


  
  print("\n>>>Updating Eye of Newt - TEST", "\n")
  botNameUpdate(f"Newt | ${newtPrice}", "eyeOfNewtBot", "test")  
  

  if (not _test):
    print("\n>>> Updating Aurum - CR", "\n")
    botNameUpdate(f"Newt | ${newtPrice}", "eyeOfNewtBot", "cr")
    '''
    print("\n>>> Updating Aurum - NFT.IT", "\n")
    botNameUpdate(f"Newt | ${newtPrice}", "eyeOfNewtBot", "nft.it")
  
  
  
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




  

  
  




