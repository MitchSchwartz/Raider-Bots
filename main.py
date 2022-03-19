import sys
from updateAllBots import updateAlltheBots
from bots_online import botList
import asyncio
import threading
import time
#from newBot.newbot import newBot

#discord logging
#logging.basicConfig(level=logging.INFO)

print(sys.version)
print(sys.version_info)

#Start Web Server
#startFlask()

#run all the things
#newBot.runNewBot()


#Bots Online
def botsOnline():

    loop = asyncio.get_event_loop()

    #Get Bots Online
    def botStart():
        for key in botList:
            try:
                loop.create_task(botList[key].client.start(botList[key].token))
            except:
                print(f"Something broke with this bot")
            else:
                print(f"{key} online")

    botStart()

    botUpdateThread = threading.Thread(target=updateAlltheBots)
    botUpdateThread.start()

    loop.run_forever()


# allBotsOnline = False
# while (not allBotsOnline):
  
#   allBotsOnline = True
#   print(allBotsOnline)
  
#   for bot in botList:
  
#     if (not botList[bot].online):
#       allBotsOnline = False
#       print(allBotsOnline)
  
#   time.sleep(1)

botsOnline()

###pretty sure nothing after here happens
