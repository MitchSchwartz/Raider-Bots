import os
import requests
from test_mode import testMode
from update_bot_name import botNameUpdate
import json
from get_server_id import serverList
import polygonscan-python

bondList = ["MR-BondBot"]




def getTokenValues():
  
  auth = os.environ.get("polygonScan")
  ids = (','.join(bondList))
  url = f'https://https://api.polygonscan.com/api?module=contract&action=getabi&address=0xee57F4C39CEfA70Ce8D07767136e5F40042CCa1b&apikey={auth}'
  
    
  
  try:
    r = requests.get(url)
    print(f"\n>>> Nomics response: {r} \n")# {dumps(r.json())}")

  except requests.exceptions.RequestException as e:
    print(f"\n {e}")# "\n", dumps(r.content), "\n")
  
  #nomicsResults = r.json()

  #print(f"\n>>>Nomics Results: {json.dumps(nomicsResults)}")

  #print(len(json.loads(r.text)))




  i=0

  while i < len(json.loads(r.text)): 
     
    if r.json()[i]['currency'] == "AURUM2":
      aP = r.json()[i]['price']

    i += 1


  
  aurumPrice = "{:10.4f}".format(float(aP))

  
  

  
  #this is probably it's own function soon
  _serverList = serverList

  if (testMode):
    _serverList = ["test"]   
  
  print(f"\n>>>testMode: {testMode}")

    
  print(f"\n>>>serverList: {_serverList}")

  for x in _serverList:    
    print(f"\n>>>x: {x}")
  
    print(f"\n>>> Updating Aurum - {x}", "\n")
    botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", x)  
    print(f"{x} - Aurumbot Updated")
    
  


  




  

  
  




