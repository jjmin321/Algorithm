# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import random

arr = []
for i in range(7):
	arr.append(random.randint(1, 9))
for i in range(1, len(arr)):
	val = arr[i]
	while i > 0 and arr[i-1] > val:
		arr[i] = arr[i-1]
		i -= 1
	arr[i]= val
print(arr)
	