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


  r = requests.patch(url, json=payload, headers=headers)
  r.json()
  

  print(f"\n>>>Name Update: {_tokenName} on {_server}\n>>>{r}\n")#>>>{dumps(r.json(), indent=4)}\n>>>")#{r.headers}")

  
'''

import discord
import asyncio
from bots_online import botList

async def testStatus(_status):
  await botList[2].change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = (_status)))
'''


