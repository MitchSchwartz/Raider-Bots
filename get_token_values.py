import os
import requests
#from time import sleep
from update_bot_name import botNameUpdate
from json import dumps
#from get_server_id import serverList

tokenList = ["RAIDER","AURUM2","GRIMWEED"]


def getTokenValues():
  
  auth = os.environ.get("nomicsKey")
  ids = (','.join(tokenList))
  url = f'https://api.nomics.com/v1/currencies/ticker?key={auth}&ids={ids}'
  
    
  
  try:
    r = requests.get(url)
    print(f"\n>>> Nomics response: {r} \n")# {dumps(r.json())}")

  except requests.exceptions.RequestException as e:
    print("\n", e, "\n", dumps(r.content), "\n")
  


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

      print("\n", ">>> gP:", gP, "\n")

    i += 1


  
  aurumPrice = "{:10.4f}".format(float(aP))

  raiderPrice = "{:10.2f}".format(float(rP))

  grimweedPrice = "{:10.2f}".format(float(gP))

  
  print(f"\n>>> Aurum: {aurumPrice} | Raider: {raiderPrice} Grimweed: {grimweedPrice} \n")



  print("\n>>>Updating Aurum - TEST", "\n")
  botNameUpdate(f"AURUM | ${aurumPrice}", "aurumBot", "test")
  
  print("\n>>> Updating Aurum - CR", "\n")
  botNameUpdate(f"AURUM | ${aurumPrice}", "aurumBot", "cr")

  print("\n>>> Updating Aurum - NFT.IT", "\n")
  botNameUpdate(f"AURUM | ${aurumPrice}", "aurumBot", "nft.it")



  print("\n>>> Updating Raider - TEST", "\n")
  botNameUpdate(f"RAIDER | ${raiderPrice}", "raiderBot", "test" )

  print("\n>>> Updating Raider - CR", "\n")
  botNameUpdate(f"RAIDER | ${raiderPrice}", "raiderBot", "cr" )

  print("\n>>> Updating Raider - NFT.IT", "\n")
  botNameUpdate(f"RAIDER | ${raiderPrice}", "raiderBot", "nft.it" )


  print("\n>>> Updating Grimweed - TEST", "\n")
  botNameUpdate(f"G-WEED | ${grimweedPrice}", "grimweedBot", "test" )

  print("\n>>> Updating Grimweed - CR", "\n")
  botNameUpdate(f"G-WEED | ${grimweedPrice}", "grimweedBot", "cr" )


  

'''
  for x in [serverList]:
    print(f"\n>>> Updating Grimweed - {x}", "\n")
    botNameUpdate(f"G-WEED | ${grimweedPrice}", "grimweedBot", x )  
    print(x)
'''
  





  

  
  




