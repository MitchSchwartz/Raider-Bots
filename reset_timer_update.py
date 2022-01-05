from datetime import datetime, timedelta
from find_date_difference import find_time_diff
import dateparser
import pytz
from update_bot_name import botNameUpdate


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

  daysLeft = 2 - now.weekday() 
  if daysLeft < 0:
    daysLeft += 7    

  timeLeft = find_time_diff(now, nextReset)

  print("timerStr: ", timeLeft)
    
  
  #botNameUpdate("Reset: " + timerStr, "timer_bot_token", "cr")
  botNameUpdate(f"Reset: {daysLeft}d {str(timeLeft)}", "timer_bot_token", "test")

  #return "timercalc done"