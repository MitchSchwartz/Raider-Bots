from test_mode import testMode

serverList = ["cr", "test", "nft.it"]



def getServerId(_server):

  if (testMode):
    serverId = '911693934231703602'

  else:  

    if _server == "cr":
      serverId = '860057024611876865'

    elif _server == "nft.it":
      serverId = '718772483729391716'
    
    else:
      serverId = '911693934231703602'
  
  return serverId