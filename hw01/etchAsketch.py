#!/usr/bin/env python3
import curses
import argparse

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
		key = stdscr.getkey()
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

curses.wrapper(main)
