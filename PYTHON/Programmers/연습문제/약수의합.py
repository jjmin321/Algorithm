'''
https://programmers.co.kr/learn/courses/30/lessons/12928

풀이 : n = xy 라면, n은 x와 y라는 약수로 이루어져있습니다. x가 n보다 크거나 같으면 y는 n보다 작거나 같습니다. 시간복잡도를 향상하기 위해 y만 구했고, y를 기반으로 x를 구했으며,
만약에 x와 y가 같은 경우(제곱수) 한 번만 계산하게 하였습니다.
'''

import math

def solution(n):
    answer = [divisor for divisor in range(1, int(math.sqrt(n)) + 1) if n % divisor == 0]
    return sum(answer) + sum([int(n/answer[i]) for i in range(len(answer)) if n != 1 and answer[i] != math.sqrt(n)])

n = 9
print(solution(n))