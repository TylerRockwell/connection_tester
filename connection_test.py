import socket
import time
import csv
from datetime import datetime, date

class Outage:
  def __init__(self, serviceType):
    self.startTime = currentTime()
    self.serviceType = serviceType
    self.endTime = None

  def finalize(self):
    self.endTime = currentTime()

  def report(self):
    if self.endTime != None:
      logEvent(self.serviceType, self.startTime, self.endTime)

def connectionIsActive(host="8.8.8.8", port=53, timeout=3):
  try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    return True
  except Exception as ex:
    return False

def connectionStatus(WANconnected, LANconnected):
    if WANconnected and LANconnected:
      return closeCurrentOutage(outage)
    elif LANconnected:
       return buildOutage("ISP")
    else:
      return buildOutage("LAN")

def buildOutage(outageType):
  return Outage(outageType)

def closeCurrentOutage(outage):
  if outage != None:
    finalizeOutage(outage)
    return None

def finalizeOutage(outage):
  outage.finalize()
  outage.report()

def logEvent(outageType, start, end):
  csv = open('outage_log.csv', 'a')
  data = buildLogData(outageType, start, end)
  csv.write(','.join(data))
  csv.write("\n")
  csv.close()

def buildLogData(outageType, start, end):
  return [
           outageType,
           readableTime(start),
           readableTime(end),
           str(timeDifference(start.time(), end.time()))
         ]

def readableTime(inputTime):
  return inputTime.strftime("%F %r")

def currentTime():
  return datetime.now().replace(microsecond=0)

def timeDifference(start, end):
  seconds = (datetime.combine(date.min, end) - datetime.combine(date.min, start)).total_seconds()
  return int(seconds)

outage = None
reporting = False
print 'Connection monitoring service started'
while True:
  try:
    WAN = connectionIsActive()
    LAN = connectionIsActive('192.168.1.1')
    outage = connectionStatus(WAN, LAN)

    time.sleep(5)
  except KeyboardInterrupt:
    print 'Connection monitoring service stopped'
    exit(0)
