""""
#!/usr/bin/env python3
# Write your name at the top, and any helpful comments you have for people
# running your program.
# By egoodale
import sys
def function_a:
# code
def function_b: # code
def main(argv):
# main method
	function_a
	function_b
main(sys.argv)
"""

def print_format_table(): 
	for style in range(8):
		for fg in range(30,38): 
			s1 = ''
			for bg in range(40,48):
				format = ';'.join([str(style), str(fg), str(bg)])
				s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
			print(s1) 
		print('\n')
print_format_table()