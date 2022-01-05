import os
import requests

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
  # check status code for response received
  # success code - 200
  print(f"\n>>>Name Update:\n>>>{r}\n>>>{r.content}\n>>>{r.headers}")
  
  # print content of request
  print(r.content)



