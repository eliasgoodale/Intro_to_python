#!/usr/bin/env python3
# By Elias Goodale

import sys
import random
import os
import time

UNDERLINE = '\x1b[4;40m'
EOC = '\x1b[0m'

def	guess_message(guess, selected, guesses):
	if guess == selected:
		print("Good Job! You are one with the Source")
		time.sleep(4)
		return True
	else:	
		if guess == "":
			print("You wasted a guess =P")
		elif len(guess) > 5:
			print("0, 1, 2, 3, 4 that's how we count to five!")
		elif guess[0] != selected[0]:x
			print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		else:
			print("You have {} left!".format(guesses - 1))
		return False

def main(argv):
	guesses = 10
	words = ['doggo', 'kitty', 'bands', 'right', 'throw']
	selected = words[random.randint(0,4)]
	finished = False
	while guesses > 0 and not finished:
		os.system('clear')
		print("Guesses: %d" % guesses)
		print("The selected word begins with %s" % selected[0].upper())
		print(UNDERLINE + "{}".format(selected[0].upper()) + "  ?  ?  ?  ?" + EOC)
		guess = input("Guess: ")
		finished = guess_message(guess, selected, guesses)
		time.sleep(2)
		guesses -= 1
	print("Bye! Thanks for playing")
	time.sleep(2)
main(sys.argv)