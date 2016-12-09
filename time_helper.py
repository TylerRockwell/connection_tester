from datetime import datetime, date, timedelta

def currentTime():
  return datetime.now().replace(microsecond=0)

def xDaysAgo(x):
  return currentTime() - timedelta(days=x)

def startOfDay(date):
  return date.replace(hour=0,minute=0,second=0)

def readableTime(inputTime):
  return inputTime.strftime("%F %r")

def readableTimeToDateTime(readableTime):
  return datetime.strptime(readableTime, "%Y-%m-%d %I:%M:%S %p")

def timeDifference(start, end):
  seconds = (datetime.combine(date.min, end) - datetime.combine(date.min, start)).total_seconds()
  return int(seconds)
