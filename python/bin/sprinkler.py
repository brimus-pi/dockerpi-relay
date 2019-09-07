#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys
import configparser
import logging

config = configparser.ConfigParser()
config.read('/home/pi/etc/sprinkler.cfg')
config.sections()

RELAY = int(config['SPRINKLER']['RELAY'])
SLT = int(config['SPRINKLER']['SLT'])
LOGLEVEL = config['LOGGING']['LEVEL']
LOGNAME = config['LOGGING']['FILE']
GPIO.setmode(GPIO.BCM)
GPIO.cleanup(RELAY)
GPIO.setup(RELAY, GPIO.OUT)

M = int(SLT / 60)

## Add logging information
logging.basicConfig(filename=LOGNAME, level=LOGLEVEL)
logging.info(" ")
logging.info("==============================================")
logging.info("Started up @ "+time.asctime())
logging.info(" ")
logging.info("Relay is on PIN {}.".format(RELAY))
logging.info("Runtime is {} seconds.".format(SLT))
logging.info("Runtime is {} minutes.".format(M))
logging.info(" ")
logging.info("{} -- TYPE = {}".format(time.asctime(), GPIO.RPI_INFO['TYPE']))
logging.info("{} -- RAM = {}".format(time.asctime(), GPIO.RPI_INFO['RAM']))
logging.info("{} -- P1_REVISION = {}".format(time.asctime(), GPIO.RPI_INFO['P1_REVISION']))
logging.info("{} -- PROCESSOR = {}".format(time.asctime(), GPIO.RPI_INFO['PROCESSOR']))
logging.info(" ")
logging.info("==============================================")
logging.info(" ")

if GPIO.input(RELAY) == 1:
    MODE = "ON"
elif GPIO.input(RELAY) == 0:
    MODE = "OFF"
else:
    GPIO.cleanup(RELAY)
    sys.exit()
logging.info("{} -- Relay {} is {}".format(time.asctime(), RELAY, MODE))

GPIO.output(RELAY, GPIO.HIGH)
if GPIO.input(RELAY) == 1:
    MODE = "ON"
elif GPIO.input(RELAY) == 0:
    MODE = "OFF"
else:
    GPIO.cleanup(RELAY)
    sys.exit()
logging.info("{} -- Relay {} is {}".format(time.asctime(), RELAY, MODE))

time.sleep(SLT)
if GPIO.input(RELAY) == 1:
    MODE = "ON"
elif GPIO.input(RELAY) == 0:
    MODE = "OFF"
else:
    GPIO.cleanup(RELAY)
    sys.exit()
logging.info("{} -- Relay {} is {}".format(time.asctime(), RELAY, MODE))

GPIO.output(RELAY, GPIO.LOW)
if GPIO.input(RELAY) == 1:
    MODE = "ON"
elif GPIO.input(RELAY) == 0:
    MODE = "OFF"
else:
    GPIO.cleanup(RELAY)
    sys.exit()
logging.info("{} -- Relay {} is {}".format(time.asctime(), RELAY, MODE))

time.sleep(1)

GPIO.cleanup(RELAY)
sys.exit()
