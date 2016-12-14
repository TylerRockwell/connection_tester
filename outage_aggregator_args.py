import optparse
from datetime import datetime

def getCommandLineArgs():
  parser = optparse.OptionParser('%prog -f <outage log csv> -m <month>')
  parser.add_option('-f',
      dest='logFile',
      type='string',
      default='outage_log.csv',
      help='Log file. CSV to read data from.')
  parser.add_option('-d',
      dest='numDays',
      type='int',
      default=7,
      help='Number of days. Enter number of days to see outages for the past x days.')
  parser.add_option('-m',
      dest='month',
      type='int',
      default=None,
      help='Numeric month field. Enter a month to see all outages for the given month.')
  parser.add_option('-s',
      dest='serviceType',
      type='string',
      default='ISP',
      help='Service to view outages for. ISP or LAN.')

  parser.add_option('-y',
      dest='year',
      type='int',
      default=datetime.now().year,
      help='Numeric year field. Defaults to current year. Format should be YYYY.')

  return parser.parse_args()

