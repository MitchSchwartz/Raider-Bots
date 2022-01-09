import os
import pytz
import requests

from datetime import datetime
from dateparser import parse as dParse
#from json import dumps

from update_bot_name import botNameUpdate
from get_server_id import getServerId
from date_functions import findTimeDiff, makeTimerStr


def tournamentTimerUpdate(_server):
  auth = "Bot " + os.environ.get(str("resetTimerBot"))

  guildId = getServerId(_server)

  url = f"https://discordapp.com/api/v9/guilds/{guildId}/scheduled-events"
  headers = {'Authorization': auth, 'Content-Type': 'application/json'}
  
  try:
    r = requests.get(url, headers=headers)
  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {r.content} \n")
    
  
  
  response = r.json()
  #print (dumps(response, indent=4))

  try:
    response.sort(key = lambda x:x["scheduled_start_time"])

    nextStart = dParse(response[0]['scheduled_start_time'])
    print(f"\n >>>next start {nextStart}")#" \n >>sorted: {dumps(response, indent =4)}\n")

    UTC = pytz.timezone('UTC')
    now = datetime.now(UTC)
    
    
    print(f"\n>>>nextStart: {nextStart}\n")
    tourneyTimeDiff, past = findTimeDiff(now, nextStart)
    print(f"\n>>>tourneyTimediff: {tourneyTimeDiff}\n")

    tourneyTimeDiff = makeTimerStr(tourneyTimeDiff)
    print(f"\n>>>tourneyTimediff2: {tourneyTimeDiff}\n")

    if past:
      tourneyTimeDiff = f"- {tourneyTimeDiff}"

    botNameUpdate(f"Duel: {tourneyTimeDiff}","tourneyBot", "test")
    botNameUpdate(f"Duel: {tourneyTimeDiff}","tourneyBot", "cr")


    #print(r.json(), r.content)

  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {r.content} \n")
    return ("! We had an problem getting events from disord")

    










