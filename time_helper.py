from datetime import datetime, date, timedelta
import calendar

def currentTime():
  return datetime.now().replace(microsecond=0)

def xDaysAgo(x):
  return currentTime() - timedelta(days=x)

def startOfDay(date):
  return date.replace(hour=0,minute=0,second=0)

def endOfDay(date):
  return date.replace(hour=23,minute=59,second=59)

def readableTime(inputTime):
  return inputTime.strftime("%B %d, %Y %I:%M:%S %p")

def csvTime(csvTime):
  return csvTime.strftime("%Y-%m-%d %I:%M:%S %p")

def csvTimeToDateTime(csvTime):
  return datetime.strptime(csvTime, "%Y-%m-%d %I:%M:%S %p")

def timeDifference(start, end):
  seconds = (datetime.combine(date.min, end) - datetime.combine(date.min, start)).total_seconds()
  return int(seconds)

def numbersToDate(monthNumber, yearNumber=currentTime().year):
  return currentTime().replace(month=monthNumber, year=yearNumber)

def startOfMonth(date):
  return startOfDay(date).replace(day=1)

def endOfMonth(date):
  lastDay = calendar.monthrange(date.year, date.month)[1]
  return endOfDay(date).replace(day=lastDay)

def inTimeRange(startTime, endTime, time):
  return time >= startTime and time <= endTime

def secondsToHMS(seconds):
  return str(timedelta(seconds=seconds))
