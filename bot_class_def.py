import discord
import os
import requests
#from time import sleep

botList ={}
testMode = os.getenv("testMode")
print(f"/n>>>testMode: {testMode}")

    
class Bot:

  def __init__(self, _name, _displayName, _symbol, _baseCurrency, _decimals, _botType):
    self.name = _name
    self.symbol = _symbol
    self.displayName = _displayName
    self.client = discord.Client()
    self.token = os.environ.get(f"{_name}")
    self.online = False
    self.runner = self.client.start(self.token)
    self.botType = _botType
    self.price = 0
    self.baseCurrency = _baseCurrency
    self.decimals = _decimals
    self.updatingNow = False

    self.serverList = []
    self.on_ready = self.client.event(self.on_ready)
    self.on_guild_join = self.client.event(self.on_guild_join)
    
    print(f"\n>>> New Bot: {self.name}\n")

  async def on_ready(self):        
    self.updateServerList()
    self.online = True
    print(f"\n>>> {self.name} > @on_ready has run")

  async def on_guild_join(self, guild):
    print('Bot has been added to a new server')     
    self.updateServerList()

    

  def updateServerList(self):
    self.updatingNow = True
    
    if (testMode == "True"):
      self.serverList = [911693934231703602]
      print(f'\n Running {self.name}.updateServerList() in testMode')

    else:      
      print(f'\nList of servers {self.name} is in: ')
      for guild in self.client.guilds:
        print(guild.name)
        if guild.id not in self.serverList:
          print(f"new guild id: {guild.name} : {guild.id}")
          self.serverList.append(guild.id)

    print(f"serverList: {self.serverList}")
    self.updatingNow = False
    
    
    

  ### BOT UPDATE METHOD ###
  def updateBot(self, _newName):
    print(f"{self.name} update function starting")
    
    self.updateServerList()
    
    # while self.updatingNow:
    #   print(f"{self.name} server list updating")
    #   sleep(1)

    
    print(f"\n>>>self.serverList: {self.serverList}")
    
    for _server in self.serverList:
      print(f"\n>>> Running updateBot {self.name} for {_server}")
      
      if(testMode == "True" and (_server != 911693934231703602 or _server =="")):
        print(f"Skipping {_server} due to Test Mode")
        return

      if(self.serverList == [] or not self.serverList):
        print(f"Skipping {_server} due to empty serverList")
        return
      

      
      auth = "Bot " + self.token
      url = f'https://discordapp.com/api/guilds/{_server}/members/@me'        
      headers = {'Authorization': auth, 'Content-Type': 'application/json'}
      payload = {'nick': _newName}
    
    
      try:  
        r = requests.patch(url, json=payload, headers=headers)
        print(f"\n>>>Name Update: {self.name} on {_server}\n>>>{r}\n")
    
    
      except requests.exceptions.RequestException as e:
        print(f"\n {e} \n {r.content} \n")
    
     

 ### (name, display name, symbol, baseCurrency, decimals, bot type)
botList = {  
  "raiderBot" : Bot(_name="raiderBot",_displayName="Raider", _symbol="RAIDER", _baseCurrency="USD", _decimals=2, _botType="token"),
  "aurumBot" : Bot("aurumBot", "Aurum", "AURUM2", "USD", 4, "token"),
  "grimweedBot" : Bot("grimweedBot", "Grmw", "GRIMWEED", "AURUM", 2, "token"),
  "eyeOfNewtBot" : Bot("eyeOfNewtBot", "Newt", "NEWT", "AURUM", 2, "token"),
  "mhpBot" : Bot("mhpBot", "MHP", "MHP2", "AURUM", 2, "token"),
  "tourneyBot" : Bot("tourneyBot", "Event", "","","", "timer"),
  "resetTimerBot" : Bot("resetTimerBot", "Reset","","","", "timer")
}


  
