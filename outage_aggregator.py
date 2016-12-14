import csv
import time_helper as timeHelper
from outage_aggregator_args import *
from time_range import *

def importData(filename='outage_log.csv'):
  with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
      data.append(row)
    return data

def entryTime(entry):
  return timeHelper.csvTimeToDateTime(entry['start_time'])

def totalDowntime(data):
  return sum(map(lambda entry: int(entry['total_time']), data))

def relevantServiceData(serviceType, data):
  return filter(lambda entry: entry['service'] == serviceType, data)

def withinTimespanData(timeRange, data):
  return filter(lambda entry: timeRange.inTimeRange(entryTime(entry)), data)

def totalOutageForService(serviceType, timeRange, data):
  return totalDowntime(withinTimespanData(timeRange, relevantServiceData(serviceType, data)))

def main():
  (options, args) = getCommandLineArgs()
  data = importData(options.logFile)

  if options.month == None:
    timeRange = TimeRange(timeHelper.xDaysAgo(options.numDays), timeHelper.currentTime())
  else:
    monthDate = timeHelper.numbersToDate(options.month, options.year)
    timeRange = TimeRange(timeHelper.startOfMonth(monthDate), timeHelper.endOfMonth(monthDate))

  outageSeconds = totalOutageForService(options.serviceType, timeRange, data)
  readableStartTime = timeHelper.readableTime(timeRange.startTime)
  readableEndTime = timeHelper.readableTime(timeRange.endTime)

  print 'Displaying total time of {} outages from {} to {}'.format(options.serviceType, readableStartTime, readableEndTime)
  print timeHelper.secondsToHMS(outageSeconds)

if __name__ == "__main__":
  main()

