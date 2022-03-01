import sys
from bots_online import botsOnline, loopForever
from newBot.newbot import newBot
from endpoints import ping, startFlask, updateAlltheBots 

#discord logging
#logging.basicConfig(level=logging.INFO)

print(sys.version)
print(sys.version_info)

#Start Web Server
startFlask()

#Bots Online
botsOnline()

#run all the things
newBot.runNewBot()
updateAlltheBots()


# #Keep the loops going I guess?
# loopForever()
