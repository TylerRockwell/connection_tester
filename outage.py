import time_helper as timeHelper

class Outage:
  def __init__(self, serviceType):
    self.serviceType = serviceType
    self.startTime = timeHelper.currentTime()
    self.endTime = None

  def finalize(self):
    self.endTime = timeHelper.currentTime()
    self.totalTime = timeHelper.timeDifference(self.startTime.time(), self.endTime.time())
