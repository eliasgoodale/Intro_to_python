import sys
USAGE = 'USAGE: python3 <program-name> num1 num2'
args = sys.argv
ac = len(args)


def div_p(a, b):
    if b != 0:
        return (a / b)
def mod_p(a, b):
    if b != 0:
        return (a % b)

def is_integer(value):
    try:
        int(value)
        return True
    except:
        return False

if ac == 3 and is_integer(args[1]) and is_integer(args[2]):
    num1 = int(args[1])
    num2 = int(args[2])
    div = int(div_p(num1, num2))
    if num1 >= num2:
        rem = mod_p(num1, num2)
    else:
        rem = 0
    a = 42
    b = float(a)
    c = False
    d = complex(a)
    varRack = ["a", "b", "c", "d"]
    varDict = dict((name,eval(name)) for name in varRack)
    print("{} divided by {} equals {} remainder {}".format(num1,num2,div,rem))
    for k, v in varDict.items():
        print("Variable {} contains: {}: {}".format(k,v, type(v)))
else:
    print(USAGE)



    
    
