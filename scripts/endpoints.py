from flask import Flask
from threading import Thread
from datetime import datetime
from time import sleep as sleep
import requests
import os

from scripts.get_token_values import getTokenValues
from scripts.tournament_timer_update import tournamentTimerUpdate
from scripts.reset_timer_update import resetTimerUpdate

testMode = os.getenv("testMode")


app = Flask('')



def updateAlltheBots():
  start = datetime.now()
  
  print("\n", f">>> RUNNING updateAlltheBots  - {start} \n")
  
  while True:
    
    
    try:
      outcomeTokenValues = getTokenValues()
    except Exception as e:
      print(f"!!!Token Bot {e} Update error  \n!!!{outcomeTokenValues}")
    
    try:    
      outcomeResetTimer = resetTimerUpdate()
    except Exception as e:
      print(f"!! resetTimer Bot Update error:\n!!{e} \n!!{outcomeResetTimer}")
    

    try:
      tournamentTimerUpdate("cr")
    except Exception as e:
      print(f"!! tournament bot error:\n {e}")
    
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

    
