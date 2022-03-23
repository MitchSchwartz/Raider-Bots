import os
import requests
from scripts.bot_class_def import botList
import functools


def priceInAurum(_tokenPrice, _aurumPrice):

    price = float(_tokenPrice) / float(_aurumPrice)
    return price


def mapTokenPrices(acc, item):

    acc[item["currency"]] = item["price"]
    return acc


def getTokenValues():
    tokenList = list(
        filter(lambda item: botList[item].symbol != "", botList.keys()))

    perPage = 1000

    auth = os.environ.get("nomicsKey")
    ids = (','.join(list(map(lambda item: botList[item].symbol, tokenList))))
    url = f'https://api.nomics.com/v1/currencies/ticker?key={auth}&per-page={perPage}&ids={ids}'

    try:
        r = requests.get(url)
        res = r.json()
        print(f"\n>>> Nomics response: {r} \n")

    except requests.exceptions.RequestException as e:
        print(f"\n {e}")

    #reduce array to currency:price key:value pairing

    tokenPrices = functools.reduce(mapTokenPrices, res, {})

    print(tokenPrices)
    # try:

    #   i=0

    #   while i < len(json.loads(r.text)):

    #     if r.json()[i]['currency'] == "AURUM2":
    #       aP = r.json()[i]['price']

    #     if r.json()[i]['currency'] == "RAIDER":
    #       rP = r.json()[i]['price']

    #     if r.json()[i]['currency'] == "GRIMWEED":
    #       gP = r.json()[i]['price']

    #     if r.json()[i]['currency'] == "NEWT":
    #       nP = r.json()[i]['price']

    #     if r.json()[i]['currency'] == "MHP2":
    #       mP = r.json()[i]['price']

    #     i += 1

    # except:
    #   print(f"\n Error processing nomics response")
    #   return("Token bot updates skipped")

    botList["aurumBot"].price = "{:10.4f}".format(float(tokenPrices["AURUM2"]))

    botList["raiderBot"].price = "{:10.2f}".format(float(tokenPrices["RAIDER"]))

    gPaP = priceInAurum(tokenPrices["GRIMWEED"], botList["aurumBot"].price)
    botList["grimweedBot"].price = "{:10.2f}".format(float(gPaP))

    nPaP = priceInAurum(tokenPrices["NEWT"], botList["aurumBot"].price)
    botList["eyeOfNewtBot"].price = "{:10.2f}".format(float(nPaP))

    mPaP = priceInAurum(tokenPrices["MHP2"], botList["aurumBot"].price)
    botList["mhpBot"].price = "{:10.2f}".format(float(mPaP))

    bPaP = priceInAurum(tokenPrices["BHP2"], botList["aurumBot"].price)
    botList["bhpBot"].price = "{:10.2f}".format(float(bPaP))


    #print(f"\n>>> Aurum: {aurumPrice} | Raider: {raiderPrice} | Grimweed: {grimweedPrice}")# | Newt: {newtPrice} \n")

    #print(f"\n>>>serverList: {_serverList}")

    # for x in _serverList:
    #   print(f"\n>>>x: {x}")

    #   #print(f"\n>>> Updating Aurum - {x}", "\n")
    #   botNameUpdate(f"Aurum | ${aurumPrice}", "aurumBot", x)
    #   #print(f"{x} - Aurumbot Updated")

    #   #print(f"\n>>> Updating Raider - {x}", "\n")
    #   botNameUpdate(f"Raider | ${raiderPrice}", "raiderBot", x )
    #   #print(f"{x} - RaiderBot Updated")

    #  #print(f"\n>>> Updating Grimweed - {x}", "\n")
    #   botNameUpdate(f"Grmw | {grimweedPrice} AUR", "grimweedBot", x)
    #   #print(f"{x} - Grimweed Updated")

    #   #print(f"\n>>> Updating Eye of Newt - {x}", "\n")
    #   botNameUpdate(f"Newt  | {newtPrice} AUR", "eyeOfNewtBot", x)
    #   #print(f"{x} - Newt Updated")

    #   #print(f"\n>>> Updating MHP - {x}", "\n")
    #   botNameUpdate(f"MHP  | {mhpPrice} AUR", "mhpBot", x)
    #   #print(f"{x} - MHP Updated")

    print("\n", botList)

    for bot in botList:
        if botList[bot].price == [] and botList[bot].type=="token":
            print(f"skipping {botList[bot].name} due to empty price value")

        if (botList[bot].baseCurrency == "USD"):
            print(f"{botList[bot].name} in USD")
            try: botList[bot].updateBot(
                f"{botList[bot].displayName} | ${botList[bot].price}")
            except Exception as e:
                print(f"\n >>> Token Bot {botList[bot].name} update error: {e}")

        elif (botList[bot].baseCurrency == "AURUM"):
            print(f"{botList[bot].name} in AUR")
            try: botList[bot].updateBot(
                f"{botList[bot].displayName} | {botList[bot].price} AUR")
            except Exception as e:
                print(f"\n >>> Token Bot {botList[bot].name} update error: {e}")

