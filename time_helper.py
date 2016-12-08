from datetime import datetime, date

def currentTime():
  return datetime.now().replace(microsecond=0)

def readableTime(inputTime):
  return inputTime.strftime("%F %r")

def timeDifference(start, end):
  seconds = (datetime.combine(date.min, end) - datetime.combine(date.min, start)).total_seconds()
  return int(seconds)
