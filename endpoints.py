from flask import Flask
from threading import Thread
from timer_calc import timerCalc
from update_bot_name import botNameUpdate


app = Flask('')


@app.route('/')
def home():
    TimerStr = timerCalc()
    botNameUpdate(TimerStr)
    return TimerStr
    

def run():
  app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()

    
