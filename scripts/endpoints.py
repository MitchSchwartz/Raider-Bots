from flask import Flask
from threading import Thread
from datetime import datetime
from time import sleep as sleep
import requests
import os

from scripts.get_token_values import getTokenValues
import scripts.tournament_timer_update as tt
from scripts.reset_timer_update import resetTimerUpdate

testMode = os.getenv("testMode")


app = Flask('')


def updateAlltheBots():
    start = datetime.now()
    print("\n", f">>> RUNNING updateAlltheBots  - {start} \n")

    tt.skipDueToRateLimit = False  # for tourney bot 429 handling

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
        if (not tt.skipDueToRateLimit or tt.skipCount > tt.skipAmount):

            try:
                tt.tournamentTimerUpdate("cr")

            except Exception as e:

                if(tt.skipCount > 0):
                    tt.skipDueToRateLimit = True
                    print(
                        f"Tournament Bot Error, retrying once before skipping {tt.skipAmount} times")

                tt.skipCount += 1
                print(f"!! tournament bot error:\n {e}")

            else:
                tt.skipCount = 0
                tt.skipDueToRateLimit = False
        else:
            tt.skipCount += 1
            print(
                f"\n>>> Skipping Tournament Bot because: recent error. skipCount is {tt.skipCount} / {tt.skipAmount}")

        if testMode == "True":
            print("\n skipping watchdog due to testMode")
        else:
            url = 'https://nosnch.in/74bee12403'
            headers = {'Content-Type': 'application/x-www-url-formencoded'}
            r = requests.post(url, headers=headers)
            print(f"Watchdog says: {r}")

        end = datetime.now()
        print(f"\n >>> updateAlltheBots Executed - {end} \n")

        sleepTime = end - start
        print(f"sleep time: {sleepTime}")
        sleep(50)


@app.route('/')
def ping():
    return('ok')


def run():
    app.run(host='0.0.0.0', port=8080)


def startFlask():
    t = Thread(target=run)
    t.start()
