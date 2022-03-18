import discord
import os
import requests
from test_mode import testMode

botList ={}


    
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

    
    
    print(f"\n>>> New Bot: {self.name}\n")

    self.serverList = []

    async def updateServerList(self):
      self.serverList =[]
      print(f'\n List of servers {self.name} is in: ')

    
      if (testMode):
        self.serverList = ["test"]

      else:
        
        for guild in self.client.guilds:
          print(guild.name)
          self.serverList.append(guild.id)

      print(f"ServerList: {self.serverList}")

    
    self.updateServerList = updateServerList(self)
    
    
    @self.client.event
    async def on_ready():        
      self.serverList = await self.updateServerList
      self.online = True
    

    async def on_guild_join(guild):
      print('Bot has been added to a new server')
      async def on_ready():        
        self.serverList = await self.updateServerList

  def updateServers(self, _newName):
    for _server in self.serverList:         
      if(testMode and (_server != "test" or _server =="")):
         return(f"Skipping {_server} due to Test Mode")

      
      auth = "Bot " + os.environ.get(str(self.tokenName))
      url = f'https://discordapp.com/api/guilds/{_server}/members/@me'        
      headers = {'Authorization': auth, 'Content-Type': 'application/json'}
      payload = {'nick': _newName}
    
    
      try:  
        r = requests.patch(url, json=payload, headers=headers)
        print(f"\n>>>Name Update: {self.tokenName} on {_server}\n>>>{r}\n")
    
    
      except requests.exceptions.RequestException as e:
        print(f"\n {e} \n {r.content} \n")
    
     


botList = {  
  "raiderBot" : Bot(_name="raiderBot",_displayName="Raider", _symbol="RAIDER", _baseCurrency="USD", _decimals=2, _botType="token"),
  "aurumBot" : Bot("aurumBot", "Aurum", "AURUM2", "USD", 4, "token"),
  "grimweedBot" : Bot("grimweedBot", "Grmw", "GRIMWEED", "AURUM", 2, "token"),
  "eyeOfNewtBot" : Bot("eyeOfNewtBot", "Newt", "NEWT", "AURUM", 2, "token"),
  "mhpBot" : Bot("mhpBot", "MHP", "MHP2", "AURUM", 2, "token"),
  "tourneyBot" : Bot("tourneyBot", "Event", "","","", "timer"),
  "resetTimerBot" : Bot("resetTimerBot", "Reset","","","", "timer")
}


  
