# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_brainstorm.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: egoodale <egoodale@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/06 11:51:36 by egoodale          #+#    #+#              #
#    Updated: 2018/06/06 14:11:16 by egoodale         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import os
import time

class term_format:
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

answer_format = term_format.GREEN
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
width = os.get_terminal_size().columns
selected_category = categories[random.randint(0,9)]

before_time = time.time()
for i in range(10):
	os.system('clear')
	print(term_format.RED + "Please write answers from the following category:\n"+ term_format.ENDC)
	print(term_format.BRED + selected_category + term_format.ENDC)
	answers.append(input(term_format.RED + "Answer %d: " % (i + 1) + term_format.ENDC))
	
after_time = time.time()

time_format = ("Time: " + str(round(after_time - before_time, 1)) + " Seconds");
answers.append(time_format);
for word in answers:
	print((answer_format +word + '\n' + term_format.ENDC).center(width))
		