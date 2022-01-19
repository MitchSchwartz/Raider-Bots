import discord
import asyncio
import os

loop = asyncio.get_event_loop()
botList ={}

def botsOnline():

  class Bot:
    
    def __init__(self, _name, _isToken ):
      self.name = _name
      self.botClient = discord.Client()
      self.token = os.environ.get(f"{_name}")
      self.online = loop.create_task(self.botClient.start(self.token))
      self.isToken = _isToken
      self.price = 0
            
      print(f"\n>>> New Bot: {self.name}")


  botList = {  
    "raiderBot" : Bot("raiderBot", True),
    "aurumBot" : Bot("aurumBot", True),
    "grimweedBot" : Bot("grimweedBot", True),
    "tourneyBot" : Bot("tourneyBot", False),
    "resetTimerBot" : Bot("resetTimerBot", False),
    "eyeOfNewtBot" : Bot("eyeOfNewtBot", True)
  }
    
    #Get Bots Online
  for key in botList:
    botList[key].online

  


def loopForever():
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
