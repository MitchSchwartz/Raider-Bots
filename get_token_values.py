import os
import requests
from update_bot_name import botNameUpdate
#import time


def getTokenValues():
  
  auth = os.environ.get("nomicsKey")
  ids = "RAIDER,AURUM2"
  url = f'https://api.nomics.com/v1/currencies/ticker?key={auth}&ids={ids}'

  r = requests.get(url)
   
  '''
  try:
    r = requests.get(url)
    print("\n", r, "\n")

  except requests.exceptions.RequestException as e:
    print("\n", e, "\n", r.content, "\n")
  '''

  if r.ok:
    print("\n", r, "\n")
  else:
    print("\n", r.content, "\n")
    raise Exception("!!! Nomics GET Request exception raised")
  

  ### Loop Thrugh Token List (Maybe I'll do this later '\_('')_/' )
  #tokenList = ["Raider", "Aurum2"]
  #for x in tokenList:
  

 

  i=0

  while i < 2:  
    if r.json()[i]['currency'] == "AURUM2":
      aP = r.json()[i]['price']

      print("\n", ">>> aP:", aP, "\n")

    if r.json()[i]['currency'] == "RAIDER":
      rP = r.json()[i]['price']

      print("\n", ">>> rP:", rP, "\n")
    

    i += 1


  
  
  aurumPrice = "{:10.4f}".format(float(aP))

  raiderPrice = "{:10.2f}".format(float(rP))

  print("\n", f">>> Aurum: {aurumPrice} | Raider: {raiderPrice}", "\n")


  print("\n>>>Updating Aurum - TEST", "\n")
  botNameUpdate(f"AURUM | ${aurumPrice}", "aurum_bot_token", "test")
  
  #print("\n>>> Updating Aurum - CR", "\n")
  #botNameUpdate(f"AURUM | ${aurumPrice}", "aurum_bot_token", "cr")
  

  print("\n>>> Updating Raider - TEST", "\n")
  botNameUpdate(f"RAIDER | ${raiderPrice}", "raider_bot_token", "test" )

  #print("\n>>> Updating Raider - CR", "\n")
  #botNameUpdate(f"RAIDER | ${raiderPrice}", "raider_bot_token", "cr" )
  





  

  
  




