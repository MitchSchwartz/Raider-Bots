import os
import requests

from get_server_id import getServerId
#from json import dumps


def botNameUpdate(_newName, _tokenName, _server):

  server = getServerId(_server)

  auth = "Bot " + os.environ.get(str(_tokenName))
  url = f'https://discordapp.com/api/guilds/{server}/members/@me'        
  headers = {'Authorization': auth, 'Content-Type': 'application/json'}
  payload = {'nick': _newName}


  try:  
    r = requests.patch(url, json=payload, headers=headers)
    #r.json()
    print(f"\n>>>Name Update: {_tokenName} on {_server}\n>>>{r}\n")#, "\n", dumps(r.json(), indent=4))#, "\n>>> {r.headers}")


  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {r.content} \n")
  


  



