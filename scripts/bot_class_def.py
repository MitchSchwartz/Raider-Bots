import discord
import os
import requests
#from time import sleep

from dotenv import load_dotenv
load_dotenv()


botList ={}
testMode = os.getenv("testMode")
print(f"/n>>>testMode: {testMode}")
testServerId = 911693934231703602
    
class Bot:

  def __init__(self, _name, _displayName, _symbol, _baseCurrency, _decimals, _botType, _enabled):
    self.name = _name
    self.symbol = _symbol
    self.displayName = _displayName
    self.client = discord.Bot()
    self.token = os.environ.get(f"{_name}")
    self.online = False    
    self.botType = _botType
    self.price = 0
    self.baseCurrency = _baseCurrency
    self.decimals = _decimals
    self.updatingNow = False
    self.enabled = _enabled
    #self.function = nameofupdatefunction


    self.serverList = []
    self.on_ready = self.client.event(self.on_ready)
    self.on_guild_join = self.client.event(self.on_guild_join)
    
    self.skip = False
    self.skipCounter = 0
    self.skipLimit = 10

    self.isFirstRun = True
    print(f"\n>>> New Bot: {self.name}\n")


  def runner(self):

    if(self.enabled == False):
      print(f"Skipping runner {self.name}; is it disabled")
      return
    
    self.client.start(self.token)
    

  async def on_ready(self):        
    self.updateServerList()
    self.online = True
    print(f"\n>>> {self.name} > @on_ready has run")

  async def on_guild_join(self, guild):
    print('Bot has been added to a new server')     
    self.updateServerList()



  def updateServerList(self):
    self.updatingNow = True
    
    if(self.enabled == False):
      print(f"Skipping {self.name}; is it disabled")
      return

    if (testMode == "True"):
      self.serverList = [testServerId]
      print(f'\n Running {self.name}.updateServerList() in testMode')

    else:      
      print(f'\nList of servers {self.name} is in: ')
      for guild in self.client.guilds:
        print(guild.name)
        if guild.id not in self.serverList and guild.id != testServerId:
          print(f"new guild id: {guild.name} : {guild.id}")
          self.serverList.append(guild.id)

    print(f"{self.name} serverList: {self.serverList}")
    self.updatingNow = False
    
    
    

  ### BOT UPDATE METHOD ###
  def updateBot(self, _newName):
    print(f"{self.name} update function starting")
    print("_newName = ", _newName)
    self.updateServerList()
    
    # while self.updatingNow:
    #   print(f"{self.name} server list updating")
    #   sleep(1)

    
    # print(f"\n>>>self.serverList: {self.serverList}")
    
    for _server in self.serverList:
      print(f"\n>>> Running updateBot {self.name} for {_server}")
      
      if(testMode == "True" and (_server != testServerId or _server =="")):
        print(f"Skipping {_server} due to Test Mode")
        return

      if(self.serverList == [] or not self.serverList):
        print(f"Skipping {_server} due to empty serverList")
        return

      if(self.enabled == False):
        print(f"Skipping {_server}; is it disabled")
        return
      

      
      auth = "Bot " + self.token
      url = f'https://discordapp.com/api/guilds/{_server}/members/@me'        
      headers = {'Authorization': auth, 'Content-Type': 'application/json'}
      payload = {'nick': _newName}
    
    
      try:  
        r = requests.patch(url, json=payload, headers=headers)
        print(f"\n>>>Name Update: {self.name} on {_server}\n>>>{r}\n")
    
    
      except requests.exceptions.RequestException as e:
        print(f"\nName update error for {self.name} on {_server}: {r} \n{e}\n")
    
     

 ### (name, display name, symbol, baseCurrency, decimals, bot type)
botList = {  
  "raiderBot" : Bot(_name="raiderBot", _displayName="Raider", _symbol="RAIDER", _baseCurrency="USD", _decimals=2, _botType="token", _enabled=True),
  "aurumBot" : Bot("aurumBot", "Aurum", "AURUM2", "USD", 4, "token",True),
  "grimweedBot" : Bot("grimweedBot", "GrmW", "GRIMWEED", "AURUM", 2, "token", True),
  "eyeOfNewtBot" : Bot("eyeOfNewtBot", "Newt", "NEWT", "AURUM", 2, "token", True),
  "mhpBot" : Bot("mhpBot", "MHP", "MHP2", "AURUM", 2, "token", True),
  "bhpBot" : Bot("bhpBot", "BHP", "BHP2", "AURUM", 2, "token", True),
  "sporebarkBot" : Bot("sporebarkBot", "SpBark", "SPOREBARK", "AURUM", 2, "token", True),
  "tourneyBot" : Bot("tourneyBot", "Event", "","","", "timer", True),
  "resetTimerBot" : Bot("resetTimerBot", "Reset","","","", "timer", True)
}

raiderBot = botList['raiderBot']
aurumBot = botList['aurumBot']
grimweedBot = botList['grimweedBot']
eyeOfNewtBot = botList['eyeOfNewtBot']
mhpBot = botList['mhpBot']
bhpBot = botList['bhpBot']
sporebarkBot = botList['sporebarkBot']
tourneyBot = botList['tourneyBot']
resetTimerBot = botList['resetTimerBot']
