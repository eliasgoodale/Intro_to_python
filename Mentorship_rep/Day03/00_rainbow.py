#!/usr/bin/env python3
# By Elias Goodale

import sys

def print_colorful_text(string, style=0, foreground=0, background=7):
	form = ';'.join([str(style), str(foreground), str(background)])
	print("\x1b[%sm%s" % (form, string), end="")

def main(argv):
	rbow = [' R ', ' A ', ' I ', ' N ', ' B ', ' O ', ' W ']
	for i in range(7):
		print_colorful_text(str(rbow[i]), style=1, foreground=(30 + i), background=(47 - i))
	print("\x1b[0m\n")

main(sys.argv)
