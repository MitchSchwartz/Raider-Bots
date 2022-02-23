import sys
from bots_online import botsOnline, loopForever
from endpoints import home, startFlask

#discord logging
#logging.basicConfig(level=logging.INFO)

print(sys.version)
print(sys.version_info)

#Start Web Server
startFlask()

#Bots Online
botsOnline()

#run all the things
home()

#Keep the loops going I guess?
loopForever()
