import sys
from bots_online import botsOnline, loopForever
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
updateAlltheBots()
newBot.runNewBot()

#Keep the loops going I guess?
loopForever()
