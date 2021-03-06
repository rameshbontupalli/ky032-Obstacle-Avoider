#!/usr/bin/env python
#---------------------------------------------------
# Author Ramesh Bontupalli
# This is a program for Infrared obstacle avoidance Module (ky032)
# It will detect the obstacle with digital output.
# Binary 0 indicates Obstacle is in vicinity. Binary 1 not obstacle detected
# 
# 
# K032 obstacle Avoidance sensor with Raspberry pi3  
# VCC -------------------- 5v (Pin 2) 
# GND -------------------- GND(Pin 6)
# SIG -------------------- GPIO 21 or Pin 40 (using Board command)
# En --------------------- N/a
#
#---------------------------------------------------

import RPi.GPIO as Ram 
import time

Ram.setwarnings(False)
# using the Board command so pin number used to declared
Ram.setmode(Ram.BOARD)
# Any GPIO can be used. I used 40 since it is easy to find.
Ram.setup(40,Ram.IN)


try:
# An inifinite loop with 500msec delay between every iteration    
    while True:
        x=Ram.input(40)
        if x==1:
            print "no obstacle"
            time.sleep(0.5)
        elif x==0:
            print "Obstacle detected"
            time.sleep(0.5)
# This is Keyboard interrupt with breaks the loop by pressing CTRL + C 
except KeyboardInterrupt:
    print "Halt"
