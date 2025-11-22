#!/usr/bin/env python
#Prova per vedere se i commit e i pull funzionano correttamente
import os
from datetime import datetime
def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20
def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    print(temperaturedata[2:])
    celsius = temperature / 1000
    return celsius
def loop(ds18b20):
    while True:
        if read(ds18b20) != None:
            now_datetime = datetime.now()
            now_datetime_str = now_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print("Current temperature : %0.3f C   [ %s ]" % (read(ds18b20), now_datetime_str))
            
def kill():
    quit()
if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
