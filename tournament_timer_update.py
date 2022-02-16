import os
import pytz
import requests


from datetime import datetime
from dateparser import parse as dParse
#from json import dumps

#from operator import itemgetter
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
    #e.sort(key=itemgetter('choice'), reverse=False)
    #print("e:", e)
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
  
  
  #print(f"\n>>>nextStart: {nextStart}\n")
  tourneyTimeDiff, past = findTimeDiff(now, nextStart)
  #print(f"\n>>>tourneyTimediff: {tourneyTimeDiff}\n")

  tourneyTimeDiff = makeTimerStr(tourneyTimeDiff)
  print(f"\n>>>tourneyTimediff2: {tourneyTimeDiff}\n")

  if past:
    tourneyTimeDiff = f"- {tourneyTimeDiff}"

  #print(r.json(), r.content)
  return tourneyTimeDiff

  
  
def tournamentTimerUpdate(_server):
  

  events = False
  events = getEvents(_server)
  newBotName = "Event: TBA"
  print(f">>>Events:{events}")

  
  if (not events):
    return

  try:
    nextStart =  getNextEventStart(events)
    #print("\n>>>there's an event!")
    newBotName = f"Event: {tourneyTimeDiff(nextStart)}"
  except requests.exceptions.RequestException as e:
    print(f"\n>>>Error: {e}")# "\n", dumps(r.content), "\n")
    
    

  for x in serverList:
    if (liveOnly and x == "test"):
      continue

    if (testMode and x != "test"):
      continue
    
    else:
      try:
        botNameUpdate(newBotName, "tourneyBot", x)
      except requests.exceptions.RequestException as e:
        print(f"\n {e} \n {r.content} \n")
    
  print("bot names updated")

    










