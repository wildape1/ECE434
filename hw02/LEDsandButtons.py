#!/usr/bin/env python3

config-pin P9_14 gpio

import Adafruit_BBIO.GPIO as GPIO
import time

up = "P8_14"
down = "P8_16"
left = "P8_12"
right = "P8_18"
reset = "P8_45"

# Set up pins as inputs or outputs
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.setup(left, GPIO.IN)
GPIO.setup(right, GPIO.IN)
GPIO.setup(reset, GPIO.IN)

GPIO.setup("P8_7", GPIO.OUT)
GPIO.setup("P8_8", GPIO.OUT)
GPIO.setup("P8_9", GPIO.OUT)
GPIO.setup("P8_10", GPIO.OUT)



def update(status):

	if status == up:
		GPIO.output(P8_7, GPIO.HIGH) = 1

	if status == down:
		GPIO.output(P8_8, GPIO.HIGH) = 1

	if status == left:
		GPIO.output(P8_9, GPIO.HIGH) = 1

	if status == right:
		GPIO.output(P8_10, GPIO.HIGH) = 1
	
	if status == reset:
		GPIO.output(P8_10, GPIO.HIGH) = 1

	else  
		GPIO.output(P8_7, GPIO.LOW) = 1
		GPIO.output(P8_8, GPIO.LOW) = 1
		GPIO.output(P8_9, GPIO.LOW) = 1
		GPIO.output(P8_10, GPIO.LOW) = 1

GPIO.add_event_detect(up, GPIO.RISING, callback=update)
GPIO.add_event_detect(down, GPIO.RISING, callback=update)
GPIO.add_event_detect(right, GPIO.RISING, callback=update)
GPIO.add_event_detect(left, GPIO.RISING, callback=update)
GPIO.add_event_detect(reset, GPIO.RISING, callback=update)


