
import esp32
import os
import wifimgr
import time
from time import sleep
import machine
 
try:
  import usocket as socket
except:
  import socket
 
led = machine.Pin(2, machine.Pin.OUT)
#wlan='ee'
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
       pass
        #pass  # you shall not pass <img draggable="false" role="img" class="emoji" alt="😀" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/1f600.svg" scale="0">
        # Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")


 
def hall_100(hall):
  print("Alert 100 - default - reset wifi and blynk")
  
    #os.remove("wifi.dat")
    
def hall_10(hall):
  print("Alert 10  -reset ")
  machine.deepsleep(10000)
 

while True:
  
 hall = esp32.hall_sensor()
 print(hall)
 if hall > 100 : hall_100(hall)
 if hall < 10 : hall_10(hall)
 time.sleep_ms(180)
