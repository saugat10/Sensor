
import humidity
import time as t
import datetime
from socket import *


serverPort = 7000

def send_udp_package(plantId, humidity, message, dateTime):
  clientSocket = socket(AF_INET, SOCK_DGRAM)
  clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
  result = '{{"plantId":1,"humidity":'+str(humidity)+',"message":'+ message +',$
  clientSocket.sendto(result.encode(),('<broadcast>', serverPort))
  clientSocket.close

while True:
  time = datetime.datetime.now()
  dateTime = time.strftime("%Y-%m-%d %H:%M:%S")
  humidity_level = humidity.humidity_check()
