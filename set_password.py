#!/usr/bin/python
import sys
import smbus
import time
bus = smbus.SMBus(0)
passwd=[d1,d2,d3,d4]
bus.write_i2c_block_data(81,123,passwd)
bus.close()
print "Password set"
