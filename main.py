
import os
import discord
import asyncio
from endpoints import home, keep_alive

#from discord.ext import commands


loop = asyncio.get_event_loop()

resetTimerBot = discord.Client()
tourneyBot = discord.Client()
grimweedBot = discord.Client()
raiderBot = discord.Client()
aurumBot = discord.Client()







#Start Web Server
keep_alive()


#@bot.command(name="schedule")
#async def setNextTourneyDT(ctx, arg):
#  updateNextTourney(arg, )
#  await ctx.channel.send(f"Tournament Scheduled for 
#  {updateNextTourney}")


#run all the things
home()



'''
botList = [
  {
    "raiderBot",
    "aurumBot",
    "grimweedBot",
    "tourneyBot", 
    "resetTimerBot"
  }
]


class Bot:
  
  def __init__(self, _name ):
    self.name = _name
    self.client = discord.Client()
    self.token = os.environ.get(f"{_name}")
    self.online = loop.create_task(self.client.start(self.token))
    print(self)


for x in botList:  
  x = Bot(x)
  print(f"bot init: {x.name}")
  #x = discord.Client()
  #xT = os.environ.get(x)
  x.online
'''






### Print 'I'm in' on connect to discord. 
@resetTimerBot.event
async def on_ready():
    print( "\n", ">>> I'm in", "\n")
    print(resetTimerBot.user)   


tToken = os.environ.get("resetTimerBot")
cToken = os.environ.get("tourneyBot")
gToken = os.environ.get("grimweedBot")
rToken = os.environ.get("raiderBot")
aToken = os.environ.get("aurumBot")

''''
tourneyBot.online
raiderBot.online
aurumBot.online
grimweedBot.online
resetTimerBot.online
'''


loop.create_task(resetTimerBot.start(tToken))
loop.create_task(tourneyBot.start(cToken))
loop.create_task(grimweedBot.start(gToken))
loop.create_task(raiderBot.start(rToken))
loop.create_task(aurumBot.start(aToken))




loop.run_forever()
