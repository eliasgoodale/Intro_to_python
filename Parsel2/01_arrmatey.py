import sys
args = sys.argv
for i in range(len(args)):
    print("Argv of %d is %s" % (i, args[i]))
args.sort(key=lambda item: (-len(item), item))
for arg in args:
    print(arg)

