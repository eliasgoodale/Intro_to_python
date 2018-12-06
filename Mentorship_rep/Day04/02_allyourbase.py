#!/usr/bin/env python3
# By Elias Goodale

import sys

def ft_bin(n):
	if n == 0:
		return ''
	else:
		return ft_bin(n // 2) + str(n % 2)

def is_integer(n):
	try:
		int(n)
		return True
	except:
		print('Not an Integer!')
		return False

def main(argv):
	if len(argv) == 2 and is_integer(argv[1]):
		print(ft_bin(int(argv[1])))

main(sys.argv)