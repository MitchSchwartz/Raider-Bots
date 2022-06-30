import os
import pytz
import requests
from scripts.bot_class_def import botList 
from scripts.date_functions import findTimeDiff, makeTimerStr

from datetime import datetime
from dateparser import parse as dParse
from json import dumps

#from operator import itemgetter






def getEvents(_server):
  auth = "Bot " + os.environ.get(str("resetTimerBot"))

  guildId = 860057024611876865

  url = f"https://discordapp.com/api/v9/guilds/{guildId}/scheduled-events"
  headers = {'Authorization': auth, 'Content-Type': 'application/json'}
  
  try:
    r = requests.get(url, headers=headers)
  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n")# {r.content} \n")
    
  print (">>>TournamentBot r: ", r)
    
  response = r.json()
  #print (dumps(response, indent=4))
  print (">>>TournamentBot Response: ", dumps(response, indent=4))
  return response



def getNextEventStart(e):

  try:
    #e.sort(key=itemgetter('choice'), reverse=False)
    print("e:", e)
    sorted(e, key = lambda x:x["scheduled_start_time"])

    nextStart = dParse(e[0]['scheduled_start_time'])
    #print(f"\n >>>next start {nextStart}")#" \n >>sorted: {dumps(response, indent =4)}\n")

    return nextStart

  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {e.content} \n")
    return ("! We had an problem getting events from discord")
    


def tourneyTimeDiff(nextStart):
  
  UTC = pytz.timezone('UTC')
  now = datetime.now(UTC)
  
  
  #print(f"\n>>>nextStart: {nextStart}\n")
  tourneyTimeDiff, past = findTimeDiff(now, nextStart)
  #print(f"\n>>>tourneyTimediff: {tourneyTimeDiff}\n")

  tourneyTimeDiff = makeTimerStr(tourneyTimeDiff)
  #print(f"\n>>>tourneyTimediff2: {tourneyTimeDiff}\n")

  if past:
    tourneyTimeDiff = f"- {tourneyTimeDiff}"

  #print(r.json(), r.content)
  return tourneyTimeDiff

  
  
def tournamentTimerUpdate(_server):
  

  events = False
  events = getEvents(_server)
  newBotName = "Event: TBA"
  #print(f">>>Events:{events}")

  
  if (not events):
    return

  try:
    nextStart =  getNextEventStart(events)
    print("\n>>>there's an event!")
    newBotName = f"Event: {tourneyTimeDiff(nextStart)}"
  except requests.exceptions.RequestException as e:
    print(f"\n>>>Error: {e}")# "\n", dumps(r.content), "\n")
    
    
  try:
    botList["tourneyBot"].updateBot({newBotName})
    print("tourney bot name updated")
  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n")
    
  

  






