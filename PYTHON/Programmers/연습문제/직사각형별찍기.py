'''
https://programmers.co.kr/learn/courses/30/lessons/12969

풀이 : 입력받은 값을 통해 순회하며 직사각형 별을 찍어 출력하였습니다.
'''

a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')
    print()