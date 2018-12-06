import sys 

USAGE = 'USAGE: python3 03_binary.py number'
def numberToBase(n, b):
	if n == 0:
		return [0]
	digits = []
	while n:
		digits.append(int(n % b))
		n //= b
	return digits[::-1]

def is_integer(value):
	try:
		int(value)
		return True
	except:
		return False
		
ac = len(sys.argv)
if ac == 2 and is_integer(sys.argv[1]):
	num = int(sys.argv[1])
	binary = numberToBase(num, 2)
	binary = ''.join(str(e) for e in binary)
	octal = numberToBase(num, 8) 
	octal = ''.join(str(e) for e in octal)
	hexadec = numberToBase(num,16)
	hexadec = ''.join(str(e) for e in hexadec)
	print("Binary: ", binary)
	print("Octal: ",octal)
	print("Hexadecimal: ",hexadec)

else:
	print(USAGE)