import socket

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

