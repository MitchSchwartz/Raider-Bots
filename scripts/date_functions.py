import datetime


def findTimeDiff(_time1, _time2):
    #print(f"\n>>>time1: {_time1} | time2: {_time2}")
    timeDiff = _time2 - _time1
    past = False
    if (timeDiff < datetime.timedelta(0)):
        timeDiff = _time1 - _time2
        past = True
    return timeDiff, past


def makeTimerStr(_timeDiff):
    _timeDiff = str(_timeDiff.days) + "d " + str(
        _timeDiff.seconds // 3600) + "h " + str(
            _timeDiff.seconds % 3600 // 60) + "m"

    # print("\n>>> Timer: ", _timeDiff, "\n")

    return _timeDiff
