from flask import Flask
from threading import Thread
from datetime import datetime
from time import sleep as sleep

from get_token_values import getTokenValues
from tournament_timer_update import tournamentTimerUpdate
from reset_timer_update import resetTimerUpdate



app = Flask('')



def updateAlltheBots():
  print("\n", f">>> RUNNING HOME  - {datetime.now()} \n")
    
  while True:

    try:
      getTokenValues()
    except:
      print("Token Bot Update error - Mitch")
    
    try:    
      resetTimerUpdate()
    except:
      print("resetTimer Bot Update error - Mitch")
    

    try:
      tournamentTimerUpdate("cr")
    except:
      print("tournament bot error, probably rate limit bullshit")
    
    print(f"\n >>> Home Executed - {datetime.now()} \n")
  
    sleep(50)

  

    



@app.route('/')
# pinged every minute by https://console.cron-job.org/dashboard
def ping(_fakeParam1, _fakeParam2):
  return('ok')
      
    
        


 


def run():
    app.run(host='0.0.0.0',port=8080)


def startFlask():
    t = Thread(target=run)
    t.start()

    
