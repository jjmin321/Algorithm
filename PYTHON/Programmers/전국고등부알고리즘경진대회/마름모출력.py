# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
cnt = 9
for i in range(1, cnt+1, 2):
	space = ' '*((cnt-i)//2)
	star = '*' * i
	print(space, star, space)
for i in range(i-2, 0, -2):
	space = ' '*((cnt-i)//2)
	star = '*' * i
	print(space, star, space)
				
		