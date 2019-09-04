#!/usr/bin/env python3

import time
import smbus
import sys
import configparser
import logging

config = configparser.ConfigParser()
config.read('../etc/water_heater.cfg')
config.sections()

RELAY = int(config['WATERHEATER']['RELAY'])
SLT = int(config['WATERHEATER']['SLT'])
DEVICE_BUS = int(config['I2C']['DEVICE_BUS'])
LOGLEVEL = config['LOGGING']['LEVEL']
LOGNAME = config['LOGGING']['FILE']
DEVICE_ADDR = 0x10

## Add logging information
logging.basicConfig(filename=LOGNAME, level=LOGLEVEL)
logging.info(" ")
logging.info("==============================================")
logging.info("Started up @ "+time.asctime())
logging.info("==============================================")
logging.info(" ")

bus = smbus.SMBus(DEVICE_BUS)

print(" ")

bus.write_byte_data(DEVICE_ADDR, RELAY, 0xFF)
print('Relay '+config['WATERHEATER']['RELAY']+' is on')
print(time.asctime())
logging.info(time.asctime()+' -- Relay '+config['WATERHEATER']['RELAY']+' is ON.')
time.sleep(SLT)

bus.write_byte_data(DEVICE_ADDR, RELAY, 0x00)
print(" ")
print('Relay '+config['WATERHEATER']['RELAY']+' is off')
print(time.asctime())
logging.info(time.asctime()+' -- Relay '+config['WATERHEATER']['RELAY']+' is OFF.')
time.sleep(1)

print(" ")

sys.exit()
