#!/usr/bin/env python3

import os
import curses
import argparse

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2b
import time
import smbus

os.system(config-pin P8_27 gpio)
os.system(config-pin P8_92 gpio)
os.system(config-pin P8_11 gpio)
os.system(config-pin P8_12 gpio)
os.system(config-pin P8_33 qep)
os.system(config-pin P8_35 qep)
os.system(config-pin P8_41 qep)
os.system(config-pin P8_42 qep)

bus = smbus.SMBus(2)
screen = 0x70

reset = "P8_11"


VEncoder = RotaryEncoder(eQEP1)
VEncoder.setAbsolute()
VEncoder.enable()

HEncoder = RotaryEncoder(eQEP2b)
HEncoder.setAbsolute()
HEncoder.enable()

# Set up pins as inputs or outputs
GPIO.setup(reset, GPIO.IN)

def setup_stage(args, stdscr):
	x_size = " "
	for x in range(args.size):
		x_size = x_size + "__"
		stdscr.addstr(3+x, 0, "|")

	stdscr.addstr(2, 0, x_size)
	stdscr.refresh()

def main(stdscr):
	# Clear screen
	stdscr.clear()
	parser = argparse.ArgumentParser()
	parser.add_argument("--size",type=int)
	args = parser.parse_args()
	setup_stage(args, stdscr)
	xcur = 3
	ycur = 2


	curses.curs_set(0)
	stdscr.addstr(0,0,"Movement: Use Buttons on BreadBoard Quit: 5th Button ",curses.A_BOLD)
	while True:
		stdscr.addstr(xcur,ycur,"X",curses.A_BOLD)
		time.sleep(0.3)
		if VEncoder.position > 0:
			stdscr.addstr(xcur,ycur,"X")
			if xcur > 3:
				xcur -= 1
		if HEncoder.position > 0:
			stdscr.addstr(xcur,ycur,"X")
			if ycur > 3:
				ycur -= 2
		if VEncoder.position < 0:
			stdscr.addstr(xcur,ycur,"X")
			if xcur < args.size+2:
				xcur += 1
		if HEncoder.position < 0:
			stdscr.addstr(xcur,ycur,"X")
			if ycur < args.size*2:
				ycur += 2
		if GPIO.input(reset):
			main(stdscr)
		stdscr.refresh()		
		HEncoder.position = 0;
		VEncoder.position = 0;
		time.sleep(0.2)


curses.wrapper(main)

