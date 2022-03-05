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
  
  try:
    i
  except:
    i=0
  
  print("\n", f">>> RUNNING updateAlltheBots  - {start} \n")
  
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
    
    
    if (i>=30 or i == 0):
      url = 'https://nosnch.in/74bee12403'
      headers = {'Content-Type': 'application/x-www-url-formencoded'}
      r = requests.post(url, headers=headers)
      print(r)
      i=0
      print(f"i: {i}")
      
    else: 
      i += 1
      print(f"i: {i}")
    
    end = datetime.now()
    print(f"\n >>> updateAlltheBots Executed - {end} \n")
    
    sleepTime = end - start
    print("sleep time")
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

    
