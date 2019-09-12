#!/usr/bin/env python3
import curses
import argparse

def setup_stage(args, stdscr):
	x_size = " "
	for x in range(args.size):
		x_size = x_size + " " + str(x)
		if x < 10:
			stdscr.addstr(2+x, 0, str(x)+" :")
		else:
			stdscr.addstr(2+x, 0, str(x)+":")
	stdscr.addstr(1, 1, x_size)
	stdscr.refresh()
	
def main(stdscr):
	# Clear screen
	stdscr.clear()
	parser = argparse.ArgumentParser()
	parser.add_argument("--size",type=int)
	args = parser.parse_args()
	if args.size > 10:
		exit()
	setup_stage(args, stdscr)
	xcur = 2
	ycur = 3
	curses.curs_set(0)
	
	while True:
		stdscr.addstr(xcur,ycur,"X",curses.A_BOLD)
		key = stdscr.getkey()
		if key == 'q':
			break
		if key == 'w':
			stdscr.addstr(xcur,ycur,"X")
			if xcur > 2:
				xcur -= 1
		if key == 'a':
			stdscr.addstr(xcur,ycur,"X")
			if ycur > 3:
				ycur -= 2
		if key == 's':
			stdscr.addstr(xcur,ycur,"X")
			if xcur < args.size+1:
				xcur += 1
		if key == 'd':
			stdscr.addstr(xcur,ycur,"X")
			if ycur < args.size*2:
				ycur += 2
		if key == 'r':
			main(stdscr)
		stdscr.refresh()

curses.wrapper(main)
