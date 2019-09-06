#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys
import configparser
import logging

config = configparser.ConfigParser()
config.read('../etc/sprinkler.cfg')
config.sections()

RELAY = int(config['SPRINKLER']['RELAY'])
LOGLEVEL = config['LOGGING']['LEVEL']
LOGNAME = config['LOGGING']['FILE']
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)

## Add logging information
logging.basicConfig(filename=LOGNAME, level=LOGLEVEL)
logging.info(" ")
logging.info("==============================================")
logging.info("Status Started up @ "+time.asctime())
logging.info("==============================================")
logging.info(" ")
logging.info("Relay is on PIN {}.".format(RELAY))
logging.info(" ")

if GPIO.input(RELAY) == 1:
    MODE = "ON"
elif GPIO.input(RELAY) == 0:
    MODE = "OFF"
else:
    sys.exit()
    
logging.info("{} -- Relay {} is {}".format(time.asctime(), RELAY, MODE))
logging.info(" ")
logging.info("{} -- TYPE = {}".format(time.asctime(), GPIO.RPI_INFO['TYPE']))
logging.info("{} -- RAM = {}".format(time.asctime(), GPIO.RPI_INFO['RAM']))
logging.info("{} -- P1_REVISION = {}".format(time.asctime(), GPIO.RPI_INFO['P1_REVISION']))
logging.info("{} -- PROCESSOR = {}".format(time.asctime(), GPIO.RPI_INFO['PROCESSOR']))

sys.exit()

