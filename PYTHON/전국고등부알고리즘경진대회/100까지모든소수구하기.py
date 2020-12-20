# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

answer = [i for i in range(2, 101)]
for number in range(2, 101):
	for divisor in range(2, int(math.sqrt(number)+1)):
		if number % divisor == 0:
			answer.remove(number)
			break
print(answer)
			