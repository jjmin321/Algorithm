'''
https://programmers.co.kr/learn/courses/30/lessons/12921

풀이 : 소수를 찾는 알고리즘은, 에라토스테네스의 체와 수의 제곱근을 이용한 공식 두 가지가 있습니다. 제곱근을 이용한 공식을 통해 풀었습니다.
'''

import math

def solution(s):
    answer = s-1
    for number in range(2, s+1):
        for divisor in range(2, int(math.sqrt(number)+1)):
            if number % divisor == 0:
                answer = answer - 1
                break
    return answer

s = 10
print(solution(s))