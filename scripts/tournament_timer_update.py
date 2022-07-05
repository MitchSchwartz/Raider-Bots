import os
import discord
from unittest import skip
import pytz
import requests
from scripts.bot_class_def import botList
from scripts.date_functions import findTimeDiff, makeTimerStr
from datetime import datetime
from dateparser import parse as dParse
#from json import dumps

#from operator import itemgetter


skipDueToRateLimit = False
skipCount = 0
skipAmount = 20



def getEvents(_server: discord.Guild):

       
    # auth = "Bot " + os.environ.get(str("resetTimerBot"))
    # guildId = 860057024611876865
  

    # url = f"https://discordapp.com/api/v9/guilds/{guildId}/scheduled-events"
    # headers = {'Authorization': auth, 'Content-Type': 'application/json'}

    try:  # GET LIST OF EVENTS
        # r = requests.get(url, headers=headers)
        r = _server.fetch_scheduled_events()
        
           
    except requests.exceptions.RequestException as e:
        print("Tournament Bot Discord Event Request Error: ", e)
        if (429 in e):
            skipDueToRateLimit = True
            return 429
        print(f"\nError getting events from Discord: {e} \n")
        return
    
    else:
        print(f"Events r = {r}")

    # response = r.json()
    print("response: ", r)
    
    #print (dumps(response, indent=4))
    
    
    if (r == []):
        return "No Events Found"
    
    print("\n>>> Discord Events response:", response)
    return response


def getNextEventStart(e):


    try:       
        e.sort(key=lambda x: x["scheduled_start_time"])


        nextStart = dParse(e[0]['scheduled_start_time'])
        print(f"\n >>>next start {nextStart}")#" \n >>sorted: {dumps(response, indent =4)}\n")

        return nextStart

    except requests.exceptions.RequestException as e:
        print(
            f"\n ! We had an problem getting events from discord: {e}")
        return


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


def tournamentTimerUpdate(_server: discord.Guild):

    # cool down period if rate limit is hit, this is a redundant check probably not stricly needed
    if (skipDueToRateLimit == True and skipCount < skipAmount):
        skipCount += 1
        return (f"\n>>> Skipped due to rate limit, Skipcount is now {skipCount}")

    events = None #reset list
    events = getEvents(_server)      
    print(f">>>Events:{events}")    
    
    if (events == 429):
        print(f"EventBot hit a 429 getting events from Discord, entering cooldown mode for {skipAmount} cycles")
        return
    
    if (events == []):
        print("Discord returned no events, skipping this round")
        return
        
    newBotName = "Event: TBA"  # I don't think this ever gets used right now

    if (not events):
        return (f"\n>>> Skipped due to: no events returned")

    try:
        nextStart = getNextEventStart(events)
        print("\n>>> We've found events!")
        newBotName = f"Event: {tourneyTimeDiff(nextStart)}"
    except requests.exceptions.RequestException as e:
        # "\n", dumps(r.content), "\n")
        print(f"\n>>> Error getting next event: {e}")

    try:
        botList["tourneyBot"].updateBot({newBotName})
        print("tourney bot name updated")
    except requests.exceptions.RequestException as e:
        print(f"\n Tournament Bot Name Update Error: {e} \n")
