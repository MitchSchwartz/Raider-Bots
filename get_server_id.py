from test_mode import testMode

serverList = {
    "cr": 860057024611876865,
    "test": 911693934231703602,
    "nft.it": 718772483729391716,
    "believers": 830224973216874516,
    "CRtools": 922572176652128296
}


def getServerId(_server):
    if (not _server or testMode):
        return serverList["test"]

    return (False)
