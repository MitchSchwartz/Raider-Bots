

def find_time_diff(_time1, _time2):
  print(f"\n>>>time1: {_time1} | time2: {_time2}")
  timeDiff = _time2 - _time1

    


  timeDiff = str(timeDiff.days) + "d " + str(timeDiff.seconds//3600) + "h " + str(timeDiff.seconds%3600//60) + "m"

  print("\n>>> Timer: ", timeDiff, "\n")

  
  return timeDiff


