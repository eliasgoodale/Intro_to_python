#!/usr/bin/env python3
# By Elias Goodale

import sys

def __min(tab):
	return min(tab)

def __max(tab):
	return max(tab)

def __mean(tab):
	return sum(tab, 0.0) / len(tab)

def __median(tab):
	arr_len = len(tab)
	center = arr_len // 2
	tab.sort()
	if not arr_len % 2:
		return (tab[center - 1] + tab[center]) / 2.0
	return tab[center]

def __mode(tab):
	return max(set(tab), key=tab.count)

def __range(tab):
	return max(tab) - min(tab)

def main(argv):
	del argv[0]
	tab = argv
	tab = list(map(int, tab))

	print("Min: %d" % __min(tab))
	print("Max: %d" % __max(tab))
	print("Mean: %.1f" % __mean(tab))
	print("Median: %d" % __median(tab))
	print("Mode: %d" % __mode(tab))
	print("Range: %d" % __range(tab))
	
main(sys.argv)