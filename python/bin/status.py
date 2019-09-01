#!/usr/bin/env python3

import smbus
import time
import sys

DB = 1
DA = 0x10
bus = smbus.SMBus(DB)

time.sleep(1)
print(" ")

for i in range(1,5):
  stat = bus.read_byte_data(DA, i)
  if stat == 255:
    mode = 'ON'
  else:
    mode = 'OFF'
  print("Status of Relay {} is {}".format(i, mode))

print(" ")
time.sleep(1)

sys.exit()
