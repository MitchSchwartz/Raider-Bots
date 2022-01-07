import os
import requests
#from time import sleep
from update_bot_name import botNameUpdate
#from json import dumps


def getTokenValues():
  
  auth = os.environ.get("nomicsKey")
  ids = "RAIDER,AURUM2,GRIMWEED"
  url = f'https://api.nomics.com/v1/currencies/ticker?key={auth}&ids={ids}'
  marketsURL = f"https://api.nomics.com/v1/markets?key={auth}&exchange=sushiswap_polygon-sushiswap-polygon&base=GRIMWEED&quote=USDT"

  #r = requests.get(url)
   
  
  try:
    r = requests.get(url)
    print("\n", r, "\n")

  except requests.exceptions.RequestException as e:
    print("\n", e, "\n", r.content, "\n")
  

  if r.ok:
    print("\n", r, "\n")
  else:
    print("\n", r.content, "\n")
    raise Exception("!!! Nomics GET Request exception raised")



  
  #sleep(2)

  try:
    m = requests.get(marketsURL)
    print("\n", m, "\n")

  except requests.exceptions.RequestException as e:
    print("\n", e, "\n", m.content, "\n")
  
  ''''

  if m.ok:
    print("\n", m, "\n")
  else:
    print("\n", m.content, "\n")
    raise Exception("!!! Nomics GET Request exception raised")
  '''

  i=0

  while i < 2:  
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


  #print(f"m.json {dumps(m.json())}")

  #gP= m.json()[0]['price']
  
  aurumPrice = "{:10.4f}".format(float(aP))

  raiderPrice = "{:10.2f}".format(float(rP))

  #grimweedPrice = "{:10.2f}".format(float(gP))

  #print(f"\n>>> Aurum: {aurumPrice} | Raider: {raiderPrice} Grimweed: {grimweedPrice} \n")


  print("\n>>>Updating Aurum - TEST", "\n")
  botNameUpdate(f"AURUM | ${aurumPrice}", "aurumBot", "test")
  
  #print("\n>>> Updating Aurum - CR", "\n")
  #botNameUpdate(f"AURUM | ${aurumPrice}", "aurumBot", "cr")
  

  print("\n>>> Updating Raider - TEST", "\n")
  botNameUpdate(f"RAIDER | ${raiderPrice}", "raiderBot", "test" )

  #print("\n>>> Updating Raider - CR", "\n")
  #botNameUpdate(f"RAIDER | ${raiderPrice}", "raiderBot", "cr" )

  #print("\n>>> Updating Grimweed - TEST", "\n")
  #botNameUpdate(f"GRIMWEED | ${grimweedPrice}", "grimweedBot", "test" )

  #print("\n>>> Updating Grimweed - CR", "\n")
  #botNameUpdate(f"RAIDER | ${raiderPrice}", "grimweedBot", "cr" )
  





  

  
  




