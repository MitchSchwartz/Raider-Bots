import pytz
import dateparser

from datetime import datetime, timedelta
from date_functions import findTimeDiff, makeTimerStr
from update_bot_name import botNameUpdate
#from get_server_id import serverList



def resetTimerUpdate():

  #Get current time in CST
  CST = pytz.timezone('Us/Central')
  now = datetime.now(CST)
  
  print ("\n", "now: ", now)
  print("\n", "now.weekday(): ", now.weekday(), "\n")

  
  #----------------------------
  ###For Testing timer changeover (reminder: re-enable 'import timedelta')
  
  #print("Testing with TOMORROW's date instead of NOW")
  #tomorrow = now + timedelta(days=1)
  
  #print("Tomorrow: ", tomorrow)
  #now=tomorrow
  #----------------------------
  

  #Calculate time difference
  nextReset = dateparser.parse('midnight, CST', settings={'PREFER_DATES_FROM': 'future'})
  
  #this next line is to adjust the weekday to wednesday
  nextReset -= timedelta(days = nextReset.weekday() -2)
  print ("\n", "findNextReset: ", nextReset, "\n")
 
  if (nextReset - now).days < 0:
      nextReset += timedelta(days = 7)

  timeLeft, past = findTimeDiff(now, nextReset)
  print("timerStr: ", timeLeft)


  timeLeft = makeTimerStr(timeLeft)  
  
  botNameUpdate(f"Reset: {str(timeLeft)}", "resetTimerBot", "cr")
  botNameUpdate(f"Reset: {str(timeLeft)}", "resetTimerBot", "test")
  botNameUpdate(f"Reset: {str(timeLeft)}", "resetTimerBot", "nft.it")

 # for x in [serverList]:
  #  botNameUpdate(f"Reset: {str(timeLeft)}", "resetTimerBot", x)
