import asyncio
from Bot import Bot
from Utilities import getTokenValues

loop = asyncio.get_event_loop()

botList = {  
  "raiderBot" : Bot("raiderBot", "Raider", "token", "RAIDER"),
  "aurumBot" : Bot("aurumBot", "Aurum", "token", "AURUM2"),
  "grimweedBot" : Bot("grimweedBot", "Grmw", "token", "GRIMWEED"),
  "eyeOfNewtBot" : Bot("eyeOfNewtBot", "Newt", "token", "NEWT"),
  "mhpBot" : Bot("mhpBot", "MHP", "token", "MHP2"),
  #"RM-BondBot" : Bot("RM-BondBot", "bond"),
  "tourneyBot" : Bot("tourneyBot", "Tourney", "timer"),
  "resetTimerBot" : Bot("resetTimerBot", "Reset", "timer")    
} 

def updateBotPrices():
  tokenValues = getTokenValues();

  for aBot in botList.values():
    if aBot.tokenKey == False:
      continue

    aBot.changeName(tokenValues[aBot.tokenKey])    
  
  
def botsOnline():
  #Get Bots Online
  for key in botList:
    try:
      #loop.create_task(botList[key].botClient.start(botList[key].token))
      botList[key].start()
    except:
      print(f"! Problem getting {key} Online")
      continue;
    
  print(f"{key} online")

  updateBotTask = loop.create_task(updateBotPrices())
  updateBotTask
  asyncio.sleep(60);
  loop.run_forever()
