from datetime import datetime
import dateparser
import pytz

def timerCalc():

  findNextReset = dateparser.parse('thursday, CST', settings={'PREFER_DATES_FROM': 'future'})

  print ("findNextReset: ",findNextReset)


  CST = pytz.timezone('Us/Central')
  now = datetime.now(CST)
    
  print ("now: ",now)
  print("now.weekday(): ",now.weekday())


  timeTillReset = findNextReset - now
  #print("timeTillReset: ", timeTillReset)


  TimerStr = str(timeTillReset.days) + "d " + str(timeTillReset.seconds//3600) + "h " + str(timeTillReset.seconds%3600//60) + "m"

  return(TimerStr)