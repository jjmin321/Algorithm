# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
numbers = [1, 1, 2, 3, 5, 8]
n = int(input())
if n > len(numbers):
	for i in range(len(numbers), n+1):
		numbers.append(numbers[len(numbers)-2] + numbers[len(numbers)-1])
print(numbers[0:n])