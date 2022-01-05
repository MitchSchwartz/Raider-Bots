import requests
import os
from update_bot_name import botNameUpdate
from find_date_difference import find_time_diff
import pytz
from datetime import datetime
from dateparser import parse as dParse
from json import dumps

def getServerID(_server):

  if _server == "cr":
    serverId = '860057024611876865'
  else:
    serverId = '911693934231703602'
  return serverId


def tournamentTimerUpdate(_server):
  auth = "Bot " + os.environ.get(str("timer_bot_token"))

  guildId = getServerID(_server)

  url = f"https://discordapp.com/api/v9/guilds/{guildId}/scheduled-events"
  headers = {'Authorization': auth, 'Content-Type': 'application/json'}
  

  r = requests.get(url, headers=headers)
  r.json()
  # check status code for response received
  # success code - 200
  print(r)

  response = r.json()
  response.sort(key = lambda x:x["scheduled_start_time"])

  nextStart = dParse(response[0]['scheduled_start_time'])
  print(f"\n >>>next start {nextStart} \n >>sorted: {dumps(response, indent =4)}\n")

  UTC = pytz.timezone('UTC')
  now = datetime.now(UTC)
  
  
  print(f"\n>>>nextStart: {nextStart}\n")
  touneyTimeDiff = find_time_diff(now, nextStart)


  print(f"\n>>>tourneyTimediff: {touneyTimeDiff}\n")

  botNameUpdate(f"⚔️ {str(touneyTimeDiff)}","tournament_timer_token", _server)


  #print(r.json(), r.content)


    










