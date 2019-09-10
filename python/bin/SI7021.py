#!/usr/bin/env python3

import time
import sys
import configparser
import logging
import board
import busio
import adafruit_si7021
import RPi.GPIO as GPIO
import gpiozero

config = configparser.ConfigParser()
config.read('/home/pi/etc/si7021.cfg')
config.sections()

INTERVAL = int(config['SI7021']['INTERVAL'])
LOGLEVEL = config['LOGGING']['LEVEL']
LOGNAME = config['LOGGING']['FILE']
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)
cpu = gpiozero.CPUTemperature()
cpu_c = cpu.temperature
cpu_f = 9 / 5 * cpu_c + 32

## Add logging information
logging.basicConfig(filename=LOGNAME, level=LOGLEVEL)
logging.info(" ")
logging.info("==============================================")
logging.info("Started up @ "+time.asctime())
logging.info("==============================================")
logging.info(" ")
logging.info("{} -- TYPE = {}".format(time.asctime(), GPIO.RPI_INFO['TYPE']))
logging.info("{} -- RAM = {}".format(time.asctime(), GPIO.RPI_INFO['RAM']))
logging.info("{} -- P1_REVISION = {}".format(time.asctime(), GPIO.RPI_INFO['P1_REVISION']))
logging.info("{} -- PROCESSOR = {}".format(time.asctime(), GPIO.RPI_INFO['PROCESSOR']))
logging.info(" ")

def getReading():
    C = sensor.temperature
    F = C * 9 / 5 + 32
    H = sensor.relative_humidity
    print("{} -- Temp F is {}".format(time.asctime(), round(F,1)))
    print("{} -- Temp C is {}".format(time.asctime(), round(C, 1)))
    print("{} -- CPU Temp F is {}".format(time.asctime(), round(cpu_f, 1)))
    print("{} -- CPU Temp C is {}".format(time.asctime(), round(cpu_c, 1)))
    print("{} -- Humidity is {}".format(time.asctime(), round(H, 1)))
    logging.info("==============================================")
    logging.info(" ")
    logging.info("{} -- Temp F is {}".format(time.asctime(), round(F, 1)))
    logging.info("{} -- Temp C is {}".format(time.asctime(), round(C, 1)))
    logging.info("{} -- CPU Temp F is {}".format(time.asctime(), round(cpu_f, 1)))
    logging.info("{} -- CPU Temp C is {}".format(time.asctime(), round(cpu_c, 1)))
    logging.info("{} -- Humidity is {}".format(time.asctime(), round(H, 1)))
    logging.info(" ")


while True:
    getReading()
    time.sleep(INTERVAL)

