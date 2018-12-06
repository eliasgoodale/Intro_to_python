# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_brainstorm.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: egoodale <egoodale@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/06 11:51:36 by egoodale          #+#    #+#              #
#    Updated: 2018/06/17 18:59:26 by egoodale         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import os
import time

class colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	RED = '\033[31m'
	BRED = '\033[31;1m'
	GREEN = '\033[32m'
	CYANBORDER = '\033[46;1m'

def	build_block(msg, maxwidth):
	block = ""
	msg_len = len(msg)
	if msg_len == maxwidth - 2:
		spaces = (maxwidth - len(msg) - 6)
	else:
		spaces = (maxwidth - len(msg) - 4)
	rear_pad = ' ' * int(spaces / 2)
	block += rear_pad
	block += msg
	i = len(block)
	while i < maxwidth:
		block += ' '
		i += 1
	return block

def border_msg(answers, maxwidth, term_width):
	print(colors.BRED)
	dash = "-" * (maxwidth + 11)
	print("+{}+".format(dash).center(term_width))
	for answer in answers:
		block = '|[\/]   '
		block += build_block(str(answer), maxwidth)
		block += '[/\]|'
		print(block.center(term_width))
	print("+{}+".format(dash).center(term_width))
	print(colors.ENDC)
	
categories = [	"US Presidents",
                "A boy's name",
                "Foods you eat for breakfast",
                "Things that are cold",
                "Insects",
                "TV Shows",
                "Things that grow",
                "School Subjects",
                "Fruits",
                "Movie titles",
                ]

answers = ["Your Answers"]
term_width = os.get_terminal_size().columns
selected_category = categories[random.randint(0,9)]

before_time = time.time()
for i in range(10):
	os.system('clear')
	print(colors.RED,"Please write answers from the following category:\n".center(term_width),colors.ENDC)
	print(colors.BRED, selected_category.center(term_width), colors.ENDC)
	answers.append(input(colors.RED + "Answer %d: " % (i + 1) + colors.ENDC))
	
after_time = time.time()

time_format = ("Time: " + str(round(after_time - before_time, 1)) + " Seconds");
answers.append(time_format);
maxwidth = len(max(answers, key=len))
formatted = '\n'.join(answers)
border_msg(answers, maxwidth + 2, term_width)
		