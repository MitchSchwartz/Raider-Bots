import os
import discord
from endpoints import keep_alive
from timer_update import timerUpdate
from get_token_values import getTokenValues
#import time

client = discord.Client()



### I forget what this does might be old
@client.event
async def on_ready():
    print( "\n", ">>> I'm in", "\n")
    print(client.user)   



#Start Web Server
keep_alive()


### Update bot nickname
#getTokenValues()


###Timer Bot Update
#timerUpdate()


#tokens = ["aurum_bot_token", "raider_bot_token", "timer_bot_token"]

ttoken = os.environ.get("timer_bot_token")
client.run(ttoken)

#token = os.environ.get("aurum_bot_token")
#client.run(token)

#rtoken = os.environ.get("raider_bot_token")
#client.run(rtoken)


#for x in tokens:
#    token = os.environ.get(x)
#    client.run(token)
#    print(str(x))

    #time.sleep(1)



  


# @client.event
# async def on_message(message):
#    if message.author != client.user:
#        await message.channel.send(message.content[::-1])


  



