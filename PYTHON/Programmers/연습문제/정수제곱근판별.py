'''
https://programmers.co.kr/learn/courses/30/lessons/12934

풀이 : n의 제곱근에서 소숫점을 자른 후 다시 제곱 계산을 합니다. 만약 그 값이 n과 같다면 n의 제곱근 + 1 의 제곱을 반환하고 아니라면 -1을 반환하였습니다.

'''

import math

def solution(n):
    return (int(math.sqrt(n)) + 1) ** 2 if int(math.sqrt(n)) ** 2 == n else -1

n = 121
print(solution(n))
