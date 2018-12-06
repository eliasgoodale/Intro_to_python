import os
import time

class tf:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    EOC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    BRED = '\033[31;1m'
    GREEN = '\033[32m'
    CYANBORDER = '\033[46;1m'
    YELLOWBORDER = '\033[33;7m'

blink1 = tf.YELLOWBORDER + tf.RED
blink2 = tf.CYANBORDER + tf.GREEN 

def scrub_alpha(word):
    ret = ""
    for i in range(len(word)):
        if word[i].isalpha():
            ret += word[i]
    return ret

def check_palindrome(word):
    i = 0
    pal_len = len(word) - 1
    while i < pal_len:
        if word[i].lower() != word[pal_len].lower(): 
            return False
        i += 1
        pal_len -= 1
    return True

pal = input("gimme pallyyyysss: ")
cut = scrub_alpha(pal)
is_pal = check_palindrome(cut) 
if is_pal:
    for i in range(10):
        os.system('clear')
        print(blink1 + "Yaas, is palindrome: {}".format(pal) + tf.EOC)
        time.sleep(.5)
        os.system('clear')
        print(blink2 + "Yaas, is palindrome: {}".format(pal[::-1]) + tf.EOC)
        time.sleep(.5)
else:
    print("Noip not palindrome")
