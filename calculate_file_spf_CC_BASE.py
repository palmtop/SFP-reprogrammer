#!/usr/bin/python
import sys
import time
if len(sys.argv)<2:
  print 'Usage '+sys.argv[0]+' filename'
  quit() 
print sys.argv[1]
f = open(sys.argv[1],"rb")
count=0
base_sum=0
while 1:
 if count>62:
  break
 byte=ord(f.read(1))
 count=count+1
 base_sum=base_sum+byte
 #print("{0:02x}:{1:02x}".format(ord(b),c)),
 print("{0:02x}".format(byte)),
 #time.sleep(0.1)
 if (count % 16) == 0:
  print
print
print "CC_BASE (0x3F,63) Hex:{0:04x} Dec:{1}".format(base_sum,base_sum%256)
#calculate CC_EXT
byte=ord(f.read(1))
count=64
base_sum=0
while 1:
 if count>94:
  break
 byte=ord(f.read(1))
 count=count+1
 base_sum=base_sum+byte
 #print("{0:02x}:{1:02x}".format(ord(b),c)),
 print("{0:02x}".format(byte)),
 #time.sleep(0.1)
 if (count % 16) == 0:
  print
f.close()
print
print "CC_EXT (0x5F,95) Hex:{0:04x} Dec:{1}".format(base_sum,base_sum%256)
