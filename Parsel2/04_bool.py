import random

POOLSIZE = 11
boolRack_1 = ["false",True,True,None,True,None,None,False,False,None,True,False]
opRack = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
boolRack_2 = [False,False,None,None,True,True,False,True,None,False,True,None]

def	ans_parser(op, bool1, bool2):
	ans = None
	if op == "or":
		ans = bool1 or bool2
	elif op == "and":
		ans = bool1 and bool2
	elif op == "==":
		ans = bool1 == bool2 
	elif op == "!=":
		ans = bool1 != bool2
	return ans

for printed_answer in range(POOLSIZE):
	Rack1_i = random.randint(0, POOLSIZE)
	Rack2_i = random.randint(0, POOLSIZE)
	op_i = random.randint(0, POOLSIZE)
	ans = ans_parser(opRack[op_i], boolRack_1[Rack1_i], boolRack_2[Rack2_i])
	print("{} {} {} => {} ".format(boolRack_1[Rack1_i], opRack[op_i], boolRack_2[Rack2_i], ans))
