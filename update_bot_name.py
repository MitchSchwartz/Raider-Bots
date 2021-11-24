import os
import requests

def botNameUpdate(_TimerStr):
  auth = "Bot " + os.environ.get("bot_token")
  url = 'https://discordapp.com/api/guilds/911693934231703602/members/@me'
  headers = {'Authorization': auth, 'Content-Type': 'application/json'}
  payload = {'nick': "Reset: " + _TimerStr}

  r = requests.patch(url, json=payload, headers=headers)
  r.json()
  # check status code for response received
  # success code - 200
  print(r)
  
  # print content of request
  print(r.content)

