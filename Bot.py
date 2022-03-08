import discord
import os

class Bot:
  
  def __init__(self, _name, _displayName, _botType, tokenKey = False):
    self.name = _name
    self.displayName = _displayName
    self.botClient = discord.Client()
    self.token = os.environ.get(f"{_name}")
    #self.online = self.botClient.start(self.token)
    self.botType = _botType
    self.price = 0
    self.tokenKey = tokenKey
          
    print(f"\n>>> New Bot: {self.name}\n")

  def start(self):
    self.botClient.start(self.token)

  def changeName(self, _name):
    newTempName = f"{self.displayName} | ${_name}"
    for server in self.discordClient.guilds:
      server.me.edit(nick=newTempName)