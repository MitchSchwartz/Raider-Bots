import discord
import asyncio
import os
import threading
from endpoints import updateAlltheBots

botList ={}

def botsOnline():
    
  class Bot:
    
    def __init__(self, _name, _botType ):
      self.name = _name
      self.botClient = discord.Client()
      self.token = os.environ.get(f"{_name}")
      self.online = self.botClient.start(self.token)
      self.botType = _botType
      self.price = 0
            
      print(f"\n>>> New Bot: {self.name}\n")


  botList = {  
    "raiderBot" : Bot("raiderBot", "token"),
    "aurumBot" : Bot("aurumBot", "token"),
    "grimweedBot" : Bot("grimweedBot", "token"),
    "eyeOfNewtBot" : Bot("eyeOfNewtBot", "token"),
    "mhpBot" : Bot("mhpBot", "token"),
    "tourneyBot" : Bot("tourneyBot", "timer"),
    "resetTimerBot" : Bot("resetTimerBot", "timer")    
  }

  botUpdateThread = threading.Thread(target=updateAlltheBots)
  botUpdateThread.start()


  loop = asyncio.get_event_loop()
  #Get Bots Online
  for key in botList:
    try:
      #botList[key].online
      loop.create_task(botList[key].botClient.start(botList[key].token))
    except:
      print(f"Something broke with this bot")
    else:
      print(f"{key} online")
      #loop.create_task(botList[key].online())
  
  loop.run_forever()

  
