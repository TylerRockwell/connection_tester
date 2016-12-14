from connection import *
import csv
from outage import *
from time import sleep
import time_helper as timeHelper

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
           timeHelper.csvTime(outage.startTime),
           timeHelper.csvTime(outage.endTime),
           str(timeHelper.timeDifference(outage.startTime.time(), outage.endTime.time()))
         ]

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
    sleep(1)
  except KeyboardInterrupt:
    print 'Connection monitoring service stopped'
    exit(0)
