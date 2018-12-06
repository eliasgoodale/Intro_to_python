#!/usr/bin/env python3
# By Elias Goodale

import sys

def get_statedict(filename):
	capitols = []
	states = []
	statedict = {}
	with open(filename) as capitols_fd:
		content = capitols_fd.readlines()
	for line in content:	
		(capitol, state) = line.split(',')
		capitols.append(capitol.rstrip('\n'))
		states.append(state.rstrip('\n'))
	for state, capitol in zip(states, capitols):
		statedict.setdefault(state, []).append(capitol)
	return statedict

def main(argv):
	statedict = get_statedict("capitols.txt")
	Done = False
	while not Done:
		choice = input("Ready: ")
		if choice == 'Done':
			break
		printed = False
		for key, val in statedict.items():
			if choice == key:
				print(str(statedict[key]).strip("['']"))
				printed = True
				break
			elif choice in str(val):
				print(key)
				printed = True
				break
		if not printed:
			print('nil')
			
main(sys.argv) 
