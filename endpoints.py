from flask import Flask
from threading import Thread

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

    
