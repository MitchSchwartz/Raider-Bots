from flask import Flask
from threading import Thread
from datetime import datetime
from time import sleep as sleep
import requests


from scripts.get_token_values import getTokenValues
from scripts.tournament_timer_update import tournamentTimerUpdate
from scripts.reset_timer_update import resetTimerUpdate




app = Flask('')



def updateAlltheBots():
  start = datetime.now()
  # i=0
  # pingFreq = 30
  
  print("\n", f">>> RUNNING updateAlltheBots  - {start} \n")
  
  while True:
    
    
    try:
      getTokenValues()
    except Exception as e:
      print(f"Token Bot Update error \n {e}")
    
    try:    
      resetTimerUpdate()
    except:
      print("resetTimer Bot Update error - Mitch")
    

    try:
      tournamentTimerUpdate("cr")
    except:
      print("tournament bot error, probably rate limit")
    
    
    ### Ping Deadman's Snitch (heroku: apps/raider-bots/resources)
    #if (i >=pingFreq or i < 1):
    url = 'https://nosnch.in/6419e9cc41'
    headers = {'Content-Type': 'application/x-www-url-formencoded'}
    r = requests.post(url, headers=headers)
    print(r)
      
      # if(i>=pingFreq):
      #   i=0
      # print(f"i: {i}")
      
    # else: 
    #   i += 1
    #   print(f"i: {i}")
    
    end = datetime.now()
    print(f"\n >>> updateAlltheBots Executed - {end} \n")
    
    sleepTime = end - start
    print(f"sleep time: {sleepTime}")
    sleep(50)

  

    



@app.route('/')
# pinged every minute by https://console.cron-job.org/dashboard
def ping():
  return('ok')
      
    
        


 


def run():
    app.run(host='0.0.0.0',port=8080)


def startFlask():
    t = Thread(target=run)
    t.start()

    
