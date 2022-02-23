from flask import Flask
from threading import Thread
from datetime import datetime

from get_token_values import getTokenValues
from tournament_timer_update import tournamentTimerUpdate
from reset_timer_update import resetTimerUpdate



app = Flask('')


@app.route('/')
# pinged every minute by https://console.cron-job.org/dashboard
def home():
    print("\n", ">>> RUNNING HOME", "\n")
    
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
    
    return('ok')
 

@app.route('/tokenbots')
def tokenbots():
    getTokenValues()


@app.route('/tourney/<nextTourney>')
#def tourneyTimer(nextTourney):
  #updateNextTourney(nextTourney)


def run():
    app.run(host='0.0.0.0',port=8080)


def startFlask():
    t = Thread(target=run)
    t.start()

    
