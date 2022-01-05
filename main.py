
import os
import discord
import asyncio
from endpoints import home, keep_alive

#from discord.ext import commands


timerBot = discord.Client()
tourneyBot = discord.Client()


### Print 'I'm in' on connect to discord. 
@timerBot.event
async def on_ready():
    print( "\n", ">>> I'm in", "\n")
    print(timerBot.user)   

#run all the things
home()

#Start Web Server
keep_alive()


#@bot.command(name="schedule")
#async def setNextTourneyDT(ctx, arg):
#  updateNextTourney(arg, )
#  await ctx.channel.send(f"Tournament Scheduled for 
#  {updateNextTourney}")


cToken = os.environ.get("timer_bot_token")
tToken = os.environ.get("tournament_timer_token")

loop = asyncio.get_event_loop()
loop.create_task(timerBot.start(tToken))
loop.create_task(tourneyBot.start(cToken))
loop.run_forever()
