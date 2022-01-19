import sys
from bots_online import botsOnline, loopForever
from endpoints import home, startFlask

#discord logging
#logging.basicConfig(level=logging.INFO)


print (sys.version)
print (sys.version_info)


#Bots Online
botsOnline()

#Start Web Server
startFlask()


#run all the things
home()

#Keep the loops going I guess?
loopForever()
