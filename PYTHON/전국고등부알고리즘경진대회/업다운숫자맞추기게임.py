# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import random 
import sys

random_number = random.randint(10, 99)
cnt = 0
for i in range(10):
	my_number = int(input())
	cnt += 1
	if my_number == random_number: 
		print("정답!", cnt)
		sys.exit()
	message = "Up!" if my_number > random_number else "Down!"
	print(message)
print("Game over!")