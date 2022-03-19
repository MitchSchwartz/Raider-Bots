from get_token_values import getTokenValues
from reset_timer_update import resetTimerUpdate
from tournament_timer_update import tournamentTimerUpdate
from datetime import datetime
import requests
from time import sleep


def updateAlltheBots():
  start = datetime.now()
  i=0
  
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
    
    pingFreq = 30
    
    if (i >=pingFreq or i < 1):
      url = 'https://nosnch.in/74bee12403'
      headers = {'Content-Type': 'application/x-www-url-formencoded'}
      r = requests.post(url, headers=headers)
      print(r)
      
      if(i>=pingFreq):
        i=0
      print(f"i: {i}")
      
    else: 
      i += 1
      print(f"i: {i}")
    
    end = datetime.now()
    print(f"\n >>> updateAlltheBots Executed - {end} \n")
    
    sleepTime = end - start
    print(f"sleep time: {sleepTime}")
    sleep(50)

  

    