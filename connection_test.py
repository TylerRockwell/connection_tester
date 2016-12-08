import socket
import time
import csv
from datetime import datetime, date

class Outage:
  def __init__(self, serviceType):
    self.serviceType = serviceType
    self.startTime = currentTime()
    self.endTime = None

  def finalize(self):
    self.endTime = currentTime()


class Connection:
  def __init__(self, host, port, timeout=3):
    self.host = host
    self.port = port
    self.timeout = timeout

  def isActive(self):
    try:
      socket.setdefaulttimeout(self.timeout)
      socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.host, self.port))
      return True
    except Exception as ex:
      return False

def currentTime():
  return datetime.now().replace(microsecond=0)

def outageType(LANconnected, WANconnected):
    return 'ISP' if LANconnected else 'LAN'

def buildOutage(outageType):
  return Outage(outageType)

def closeCurrentOutage(outage):
  if outage != None:
    finalizeOutage(outage)
    return None

def finalizeOutage(outage):
  outage.finalize()
  logEvent(outage)

def logEvent(outage):
  csv = open('outage_log.csv', 'a')
  data = buildLogData(outage)
  csv.write(','.join(data))
  csv.write("\n")
  csv.close()

def buildLogData(outage):
  return [
           outage.serviceType,
           readableTime(outage.startTime),
           readableTime(outage.endTime),
           str(timeDifference(outage.startTime.time(), outage.endTime.time()))
         ]

def readableTime(inputTime):
  return inputTime.strftime("%F %r")


def timeDifference(start, end):
  seconds = (datetime.combine(date.min, end) - datetime.combine(date.min, start)).total_seconds()
  return int(seconds)

outage = None
WAN = Connection('8.8.8.8', 53)
LAN = Connection('192.168.1.1', 53)
print 'Connection monitoring service started'
while True:
  try:
    if LAN.isActive() and WAN.isActive():
      outage = closeCurrentOutage(outage)
    else:
      failurePoint = outageType(LAN.isActive(), WAN.isActive())
      outage = outage or buildOutage(failurePoint)
    time.sleep(1)
  except KeyboardInterrupt:
    print 'Connection monitoring service stopped'
    exit(0)
