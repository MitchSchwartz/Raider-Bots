import os
import discord
from endpoints import keep_alive
from update_bot_name import botNameUpdate
from timer_calc import timerCalc

client = discord.Client()



### I forget what this does might be old
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)    


keep_alive()


###Timer Calculation
TimerStr = timerCalc()


### Update bot nickname
botNameUpdate(TimerStr)

token = os.environ.get("bot_token")
client.run(token)
  


# @client.event
# async def on_message(message):
#    if message.author != client.user:
#        await message.channel.send(message.content[::-1])


  



