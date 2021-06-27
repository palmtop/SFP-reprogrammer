#!/usr/bin/python
import sys
import smbus
import time
from datetime import timedelta
outFile = open("chkpw.log","w")
count=0
t=time.time()
bus = smbus.SMBus(0)
#in range the top is not included!
#symbols=list(range(48,58))+list(range(65,91))+list(range(97,123))
#symbols=range(48,58)
symbols=range(0,256)
start_symbol=range(0,256)
total=len(start_symbol)*len(symbols)*len(symbols)*len(symbols)
#total=len(symbols)*len(symbols)*len(symbols)
#We are testing on the first character of the manufacturer name
#We write one character higher, and check if it has changed
test_ch=bus.read_byte_data(80,20)+1 
for d1 in start_symbol:
 bus.write_byte_data(81,123,d1)
 for d2 in symbols:
  bus.write_byte_data(81,124,d2)
  for d3 in symbols:
   bus.write_byte_data(81,125,d3)
   for d4 in symbols:
    bus.write_byte_data(81,126,d4)
    #passwd=[d1,d2,d3,d4]
    #bus.write_i2c_block_data(81,123,passwd)
    bus.write_byte_data(80,20,test_ch)
    #print(count,"{0:02x}:{1:02x}:{2:02x}:{3:02x}".format(d1,d2,d3,d4))
    count=count+1
   c = bus.read_byte_data(80,20)
   if c!=(test_ch-1):
    print(d1,d2,d3,d4)
    print("{0:02x}:{1:02x}:{2:02x}:{3:02x}".format(d1,d2,d3,d4))
    print(c)
    print ("Passwd-block", d1,d2,d3,d4,file=outFile)
    for d4 in symbols:
     bus.write_byte_data(81,126,d4)
     bus.write_byte_data(80,20,test_ch-1)
     c = bus.read_byte_data(80,20)
     if c==(test_ch-1):
      print("Passwd: ",d1,d2,d3,d4)
      print("Passwd: ","{0:02x}:{1:02x}:{2:02x}:{3:02x}".format(d1,d2,d3,d4))
      print(c)
      print ("Passwd", d1,d2,d3,d4,"{0:02x}:{1:02x}:{2:02x}:{3:02x}".format(d1,d2,d3,d4),file=outFile)
      outFile.close()
      bus.close()
      quit()
  t1=time.time()
  speed=(len(symbols)*len(symbols))/(t1-t)
  print(count,"Percent: {0:.02%} Speed: {1:.2f} Total: {2} Remaining:".format((count+0.0)/total,speed,total), timedelta(seconds=(total-count)/speed))
  if (d2%4==0):
   print (d1,d2,d3,d4,file=outFile)
   outFile.flush()
  t=t1
outFile.close()
bus.close()
print
