from flask import Flask
from threading import Thread
from datetime import datetime
from time import sleep as sleep
import requests


from get_token_values import getTokenValues
from tournament_timer_update import tournamentTimerUpdate
from reset_timer_update import resetTimerUpdate




app = Flask('')



def updateAlltheBots():
  start = datetime.now()
  print("\n", f">>> RUNNING updateAlltheBots  - {start} \n")
    
  while True:
    i = 0
    
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
    
    
    if (i>30):
      url = 'https://nosnch.in/74bee12403'
      headers = {'Content-Type': 'application/x-www-url-formencoded'}
      r = requests.post(url, headers=headers)
      i=0
      print(f"{i}")
    else: 
      i += 1
      print(f"{i}")
    
    end = datetime.now()
    print(f"\n >>> updateAlltheBots Executed - {end} \n")
    
    
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

    
