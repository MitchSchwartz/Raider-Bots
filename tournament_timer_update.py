import os
import pytz
import requests

from datetime import datetime
from dateparser import parse as dParse
#from json import dumps

from update_bot_name import botNameUpdate
from get_server_id import getServerId, serverList
from date_functions import findTimeDiff, makeTimerStr
from test_mode import testMode, liveOnly




def getEvents(_server):
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
  return response



def getNextEventStart(e):

  try:
    e.sort(key = lambda x:x["scheduled_start_time"])

    nextStart = dParse(e[0]['scheduled_start_time'])
    print(f"\n >>>next start {nextStart}")#" \n >>sorted: {dumps(response, indent =4)}\n")

    return nextStart

  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {e.content} \n")
    return ("! We had an problem getting events from disord")
    


def tourneyTimeDiff(nextStart):
  
  UTC = pytz.timezone('UTC')
  now = datetime.now(UTC)
  
  
  print(f"\n>>>nextStart: {nextStart}\n")
  tourneyTimeDiff, past = findTimeDiff(now, nextStart)
  print(f"\n>>>tourneyTimediff: {tourneyTimeDiff}\n")

  tourneyTimeDiff = makeTimerStr(tourneyTimeDiff)
  print(f"\n>>>tourneyTimediff2: {tourneyTimeDiff}\n")

  if past:
    tourneyTimeDiff = f"- {tourneyTimeDiff}"

  #print(r.json(), r.content)
  return tourneyTimeDiff

  
  
def tournamentTimerUpdate(_server):
  events = getEvents(_server)
  nextStart =  getNextEventStart(events)
  newBotName = tourneyTimeDiff(nextStart)
  
  for x in serverList:
    if (x == "test" and liveOnly):
      continue

    if (x != "test" and testMode):
      continue
    
    else:
      botNameUpdate(f"Event: {newBotName}","tourneyBot", x)
    
  print("bot names updated")

    










