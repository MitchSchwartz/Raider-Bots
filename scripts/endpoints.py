from flask import Flask
from threading import Thread
from datetime import datetime
from time import sleep as sleep
import requests
import os

from scripts.get_token_values import getTokenValues
from scripts.tournament_timer_update import tournamentTimerUpdate
from scripts.reset_timer_update import resetTimerUpdate
from scripts.bot_class_def import botList

testMode = os.getenv("testMode")
tourneyBot = botList['tourneyBot']

app = Flask('')


def updateAlltheBots():
    start = datetime.now()
    print("\n", f">>> RUNNING updateAlltheBots  - {start} \n")

    skipDueToRateLimit = False  # for tourney bot 429 handling

    while True:  # forever

        ### Token Bots ###
        try:
            outcomeTokenValues = getTokenValues()
        except Exception as e:
            print(f"!!!Token Bot {e} Update error  \n!!!{outcomeTokenValues}")

        ### Reset Timer Bot ###
        try:
            outcomeResetTimer = resetTimerUpdate()
        except Exception as e:
            skipDueToRateLimit = True
            print(
                f"!! resetTimer Bot Update error:\n!!{e} \n!!{outcomeResetTimer}")

        ### Tournament Timer Bot Update ###
        if (not tourneyBot.skip or tourneyBot.skipCounter > tourneyBot.skipLimit ):
            try:
                tournamentTimerUpdate("cr")

            except Exception as e:
                print("Tournament Bot update error: ", e)


        else:
            tourneyBot.skipCounter +=1


    
    
        if testMode =="True":
            print("\n skipping watchdog due to testMode")
        
        else:
            url = 'https://nosnch.in/74bee12403'
            headers = {'Content-Type': 'application/x-www-url-formencoded'}
            r = requests.post(url, headers=headers)
            print(r)
            
        end = datetime.now()
        print(f"\n >>> updateAlltheBots Executed - {end} \n")
        
        sleepTime = end - start
        print(f"sleep time: {sleepTime}")
        sleep(50)

  

    



@app.route('/')

def ping():
  return('ok')
           


def run():
    app.run(host='0.0.0.0',port=8080)


def startFlask():
    t = Thread(target=run)
    t.start()

    
