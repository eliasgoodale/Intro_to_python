#!/usr/bin/env python3
# By Elias Goodale

import sys

BRED = '\033[1;31m'
EOC = '\033[0m'

def get_names(filename):
	fnames = []
	lnames = []
	with open(filename) as names_fd:
		fullnames = names_fd.readlines()
	for line in fullnames:
		(fn, ln) = line.split(',')
		fnames.append(fn.rstrip('\n'))
		lnames.append(ln.rstrip('\n'))
	return fnames, lnames

def print_key_lastname(fnames, lnames):
	ln_Phonebook = {}
	for val, key in zip(fnames, lnames):
		ln_Phonebook.setdefault(key, []).append(val)
	print(BRED,"\n** Shared Last Names! **\n",EOC)
	for key, val in ln_Phonebook.items():
		if len(val) > 1:
			print(key, "({})".format(len(val)), val)

def print_key_firstname(fnames, lnames):
	fn_Phonebook = {}
	for key, val in zip(fnames, lnames):
		fn_Phonebook.setdefault(key, []).append(val)
	print(BRED,"\n** Shared First Names! **\n",EOC)
	for key, val in fn_Phonebook.items():
		if len(val) > 1:
			print(key, "({})".format(len(val)), val)

def main(argv):
	fnames, lnames = get_names("names.txt")
	print_key_firstname(fnames, lnames)
	print_key_lastname(fnames, lnames)
				
main(sys.argv)