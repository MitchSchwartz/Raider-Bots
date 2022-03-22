import sys
from endpoints import updateAlltheBots, startFlask
from bot_class_def import botList
import asyncio
import threading


#discord logging
#logging.basicConfig(level=logging.INFO)

print(sys.version)
print(sys.version_info)

#Start Web Server
startFlask()


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



botsOnline()

###pretty sure nothing after here happens
