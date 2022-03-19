from flask import Flask
from threading import Thread
from datetime import datetime
from time import sleep as sleep
import requests


from get_token_values import getTokenValues
from tournament_timer_update import tournamentTimerUpdate
from reset_timer_update import resetTimerUpdate




app = Flask('')






@app.route('/')
# pinged every minute by https://console.cron-job.org/dashboard
def ping(_fakeParam1, _fakeParam2):
  return('ok')
      
    
        


 


def run():
    app.run(host='0.0.0.0',port=8080)


def startFlask():
    t = Thread(target=run)
    t.start()

    
