#!/usr/bin/env python3

import os
import curses
import argparse

import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2b
import time
import smbus

os.system("config-pin P8_11 gpio")
os.system("config-pin P8_12 gpio")
os.system("config-pin P8_33 qep")
os.system("config-pin P8_35 qep")
os.system("config-pin P8_41 qep")
os.system("config-pin P8_42 qep")

bus = smbus.SMBus(2)
matrix = 0x70
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

reset = "P8_11"

VEncoder = RotaryEncoder(eQEP1)
VEncoder.setAbsolute()
VEncoder.enable()

HEncoder = RotaryEncoder(eQEP2b)
HEncoder.setAbsolute()
HEncoder.enable()

# Set up pins as inputs or outputs
GPIO.setup(reset, GPIO.IN)

output = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

def update(output, xcur, ycur):
	row = xcur * 2
	column = 2**ycur
	output[row] |= column
	return output

xcur = 0
ycur = 0
row = 0
while True:

	time.sleep(0.1)
	if VEncoder.position > 0:
		ycur += 1
		if ycur > 7:
			ycur = 7
		output = update(output, xcur, ycur)

	if HEncoder.position > 0:
		xcur += 1
		if xcur > 7:
			xcur = 7
		output = update(output, xcur, ycur)

	if VEncoder.position < 0:
		ycur -= 1
		if ycur < 0:
			ycur = 0
		output = update(output, xcur, ycur)

	if HEncoder.position < 0:
		xcur -= 1
		if xcur < 0:
			xcur = 0
		output = update(output, xcur, ycur)

	if not GPIO.input(reset):
		output = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
		xcur = 0
		ycur = 0

	HEncoder.position = 0;
	VEncoder.position = 0;
	bus.write_i2c_block_data(matrix, 0, output)
