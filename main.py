import sys
from scripts.endpoints import updateAlltheBots, startFlask
from scripts.bot_class_def import botList
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
              if(key.enabled == False):
                print(f"Skipping {key}; is it disabled")
                return   
                
              loop.create_task(botList[key].client.start(botList[key].token))
              
            except:
                print(f"{key} couldn't get online")
            else:
                print(f"{key} online")

    botStart()

    botUpdateThread = threading.Thread(target=updateAlltheBots)
    botUpdateThread.start()

    loop.run_forever()
    ###nothing runs after this



botsOnline()

###pretty sure nothing after here happens
