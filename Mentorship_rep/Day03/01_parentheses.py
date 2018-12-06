#!/usr/bin/env python3
# By Elias Goodale

import sys

def capitalize_other(string):
	ret = ""
	i = True
	for c in string:
		if i:
			ret += c.upper() 
		else:
			ret += c.lower()
		if c.isalpha():
			i = not i
	return ret

def star_other_upcase_vowel(string):
	vowels = "AEIOU"
	ret = ""
	for c in string:
		if c in vowels and c.isupper():
			ret += '*'
		else:
			ret += c
	return ret

def check_parenth_balance(string):
	open_count = 0
	close_count = 0
	for c in string:
		if c == '(':
			open_count += 1
		elif c == ')':
			close_count += 1
	return open_count == close_count
		
def main(argv):
	ac = len(argv)
	print(ac)
	if ac == 2:
		print(capitalize_other(argv[1]))
		print(star_other_upcase_vowel(capitalize_other(argv[1])))
		print("Balanced? {}".format(check_parenth_balance(argv[1])))

main(sys.argv)