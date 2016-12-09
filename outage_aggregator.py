import csv
import time_helper as timeHelper

def importData(filename='outage_log.csv'):
  with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
      data.append(row)
    return data

def totalDowntime(data):
  return sum(map(lambda entry: int(entry['total_time']), data))

def relevantServiceData(serviceType, data):
  return filter(lambda entry: entry['service'] == serviceType, data)

def withinTimespanData(numDays, data):
  startDate = timeHelper.startOfDay(timeHelper.xDaysAgo(numDays))
  return filter(lambda entry: timeHelper.readableTimeToDateTime(entry['start_time']) >= startDate, data)

def totalOutageForService(serviceType, numDays, data):
  return totalDowntime(withinTimespanData(numDays, relevantServiceData(serviceType, data)))

data = importData()
print totalOutageForService('LAN', 7, data)

