import discord
import asyncio
import os

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
    #"RM-BondBot" : Bot("RM-BondBot", "bond"),
    "tourneyBot" : Bot("tourneyBot", "timer"),
    "resetTimerBot" : Bot("resetTimerBot", "timer")    
  }

  loop = asyncio.get_event_loop()
  #Get Bots Online
  for key in botList:
    print(f"{key} online")
    loop.create_task(botList[key].online())
  
  loop.run_forever()

  

# A Loop  I would like to do instead
'''
for x in botList:  
  x = Bot(f"{x}")
  print(f"bot init: {x.name}")
  #x = discord.Client()
  #xT = os.environ.get(x)
  #x.online
  #sleep(1)
'''
