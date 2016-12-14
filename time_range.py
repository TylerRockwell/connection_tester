class TimeRange:
  def __init__(self, startTime, endTime):
    self.startTime = startTime
    self.endTime = endTime

  def inTimeRange(self, time):
    return time >= self.startTime and time <= self.endTime
