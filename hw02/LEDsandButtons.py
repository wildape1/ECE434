#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
set = 1000
up = "P8_14"
down = "P8_16"
left = "P8_12"
right = "P8_18"
reset = "P8_11"

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
		GPIO.output("P8_7", GPIO.HIGH)

	if status == down:
		GPIO.output("P8_8", GPIO.HIGH)

	if status == left:
		GPIO.output("P8_9", GPIO.HIGH)

	if status == right:
		GPIO.output("P8_10", GPIO.HIGH)

	if status == status:
		set = 1000

	if status == reset:
		print("reset")
		GPIO.output("P8_7", GPIO.LOW)
		GPIO.output("P8_8", GPIO.LOW)
		GPIO.output("P8_9", GPIO.LOW)
		GPIO.output("P8_10", GPIO.LOW)

update(set)
GPIO.add_event_detect(up, GPIO.RISING, bouncetime=200, callback=update)
GPIO.add_event_detect(down, GPIO.RISING, bouncetime=200, callback=update)
GPIO.add_event_detect(right, GPIO.RISING, bouncetime=200, callback=update)
GPIO.add_event_detect(left, GPIO.RISING, bouncetime=200, callback=update)
GPIO.add_event_detect(reset, GPIO.RISING, bouncetime=200, callback=update)

while True:
	time.sleep(100)
