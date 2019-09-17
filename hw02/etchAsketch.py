#!/usr/bin/env python3

import curses
import argparse

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
	stdscr.addstr(0,0,"Movement: W A S D Restart: r Quit: q",curses.A_BOLD)
	while True:
		stdscr.addstr(xcur,ycur,"X",curses.A_BOLD)
		#key = stdscr.getkey()
		if key == 'q':
			break
		if key == 'w':
			stdscr.addstr(xcur,ycur,"X")
			if xcur > 3:
				xcur -= 1
		if key == 'a':
			stdscr.addstr(xcur,ycur,"X")
			if ycur > 3:
				ycur -= 2
		if key == 's':
			stdscr.addstr(xcur,ycur,"X")
			if xcur < args.size+2:
				xcur += 1
		if key == 'd':
			stdscr.addstr(xcur,ycur,"X")
			if ycur < args.size*2:
				ycur += 2
		if key == 'r':
			main(stdscr)
		stdscr.refresh()

def update(status):

	if status == up:
		GPIO.output("P8_7", GPIO.HIGH)
		key = 'w'

	if status == down:
		GPIO.output("P8_8", GPIO.HIGH)
		key = 's'

	if status == left:
		GPIO.output("P8_9", GPIO.HIGH)
		key = 'a'

	if status == right:
		GPIO.output("P8_10", GPIO.HIGH)
		key = 'd'

	if status == reset:
		print("reset")
		GPIO.output("P8_7", GPIO.LOW)
		GPIO.output("P8_8", GPIO.LOW)
		GPIO.output("P8_9", GPIO.LOW)
		GPIO.output("P8_10", GPIO.LOW)
		key = 'r'

GPIO.add_event_detect(up, GPIO.RISING, bouncetime=200, callback=update)
GPIO.add_event_detect(down, GPIO.RISING, bouncetime=200, callback=update)
GPIO.add_event_detect(right, GPIO.RISING, bouncetime=200, callback=update)
GPIO.add_event_detect(left, GPIO.RISING, bouncetime=200, callback=update)
GPIO.add_event_detect(reset, GPIO.RISING, bouncetime=200, callback=update)

curses.wrapper(main)

