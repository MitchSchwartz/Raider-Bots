import os
import requests
from scripts.bot_class_def import botList
import functools
from json import dumps

from dotenv import load_dotenv
load_dotenv()


def priceInAurum(_tokenPrice):

    price = float(_tokenPrice) / float(botList["aurumBot"].price)
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

    print(f"tokenPrices: {tokenPrices}")

    
    for bot in botList:
      print(bot)
  
      if botList[bot].botType == "token":
  
        rawPrice = float(tokenPrices[botList[bot].symbol])
        decimal = "{:10."+f"{botList[bot].decimals}"+"f}"
        
        print("decimal: ", decimal," | RawPrice", rawPrice)
        
        
        
        if botList[bot].baseCurrency == "AURUM":
          botList[bot].price = decimal.format(priceInAurum(rawPrice))

        else:
          botList[bot].price =  decimal.format(rawPrice)
          
        print(botList[bot].symbol,", ", botList[bot].price,", price")
      
      
  
    # botList["aurumBot"].price = "{:10.4f}".format(float(tokenPrices["AURUM2"]))

    # botList["raiderBot"].price = "{:10.2f}".format(float(tokenPrices["RAIDER"]))

    # gPaP = priceInAurum(tokenPrices["GRIMWEED"], botList["aurumBot"].price)
    # botList["grimweedBot"].price = "{:10.2f}".format(float(gPaP))

    # nPaP = priceInAurum(tokenPrices["NEWT"], botList["aurumBot"].price)
    # botList["eyeOfNewtBot"].price = "{:10.2f}".format(float(nPaP))

    # mPaP = priceInAurum(tokenPrices["MHP2"], botList["aurumBot"].price)
    # botList["mhpBot"].price = "{:10.2f}".format(float(mPaP))

    # bPaP = priceInAurum(tokenPrices["BHP2"], botList["aurumBot"].price)
    # botList["bhpBot"].price = "{:10.2f}".format(float(bPaP))

    # sPaP = priceInAurum(tokenPrices["SPOREBARK"], botList["sporebarkBot"].price)
    # botList["sporebarkBot"].price = "{:10.2f}".format(float(sPaP))


    

    for bot in botList:
        if botList[bot].price == [] and botList[bot].type=="token":
            print(f"skipping {botList[bot].name} due to empty price value")

        if (botList[bot].baseCurrency == "USD"):
            print(f"{botList[bot].name} in USD")
            try: botList[bot].updateBot(
                f"{botList[bot].displayName} | ${botList[bot].price}")
            except Exception as e:

                raise f"\n >>> Token Bot {botList[bot].name} update error: {e}"


        elif (botList[bot].baseCurrency == "AURUM"):
            print(f"{botList[bot].name} in AUR")
            try: botList[bot].updateBot(
                f"{botList[bot].displayName} | {botList[bot].price} AUR")
            except Exception as e:

                return(f"\n >>> Token Bot {botList[bot].name} update error: {e}")
                raise

