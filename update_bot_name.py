import os
import requests
#from json import dumps

def botNameUpdate(_newName, _tokenName, _server):

  if _server == "cr":
      _url = 'https://discordapp.com/api/guilds/860057024611876865/members/@me'      
  else:
    _url = 'https://discordapp.com/api/guilds/911693934231703602/members/@me'



  auth = "Bot " + os.environ.get(str(_tokenName))
  url = _url
  headers = {'Authorization': auth, 'Content-Type': 'application/json'}
  payload = {'nick': _newName}


  r = requests.patch(url, json=payload, headers=headers)
  r.json()
  

  print(f"\n>>>Name Update: {_tokenName} on {_server}\n>>>{r}\n>>>")#{dumps(r.json(), indent=4)}\n>>>")#{r.headers}")
  
  # print content of request




