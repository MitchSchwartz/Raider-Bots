import sys
import threading
from bots_online import botsOnline#, loopForever
#from newBot.newbot import newBot
from endpoints import ping, startFlask, updateAlltheBots 

#discord logging
#logging.basicConfig(level=logging.INFO)

print(sys.version)
print(sys.version_info)

#Start Web Server
#startFlask()

#Bots Online
botThread = threading.Thread(target=botsOnline)
botThread.start()

#run all the things
#newBot.runNewBot()
botUpdateThread = threading.Thread(target=updateAlltheBots)
botUpdateThread.start()


# #Keep the loops going I guess?
# loopForever()
