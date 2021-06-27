#!/usr/bin/python
import sys
import smbus
import time
count=0
t=time.time()
bus = smbus.SMBus(0)
symbols=range(48,58)+range(65,91)+range(97,123)
#symbols=range(48,58)
total=len(symbols)*len(symbols)*len(symbols)*len(symbols)
#total=len(symbols)*len(symbols)*len(symbols)
d4=48
for d1 in symbols:
 for d2 in symbols:
  for d3 in symbols:
   for d4 in symbols:
    passwd=[d1,d2,d3,d4]
    bus.write_i2c_block_data(81,123,passwd)
    bus.write_byte_data(80,20,ord("M"))
    c = bus.read_byte_data(80,20)
    #print(count,"{0:02x}:{1:02x}:{2:02x}:{3:02x}".format(d1,d2,d3,d4))
    if c!=76:
     print(d1,d2,d3,d4)
     print("{0:02x}:{1:02x}:{2:02x}:{3:02x}".format(d1,d2,d3,d4))
     print(c)
     quit()
    count=count+1
    if (count%1000==0):
     t1=time.time()
     speed=1000/(t1-t)
     print(count,"Percent: {0:.02%} Speed: {1:.2f} Total: {2}".format((count+0.0)/total,speed,total))
     t=t1
bus.close()
print
