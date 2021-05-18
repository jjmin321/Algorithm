'''
https://programmers.co.kr/learn/courses/30/lessons/42842

풀이 : 먼저 brown+yellow의 약수를 구합니다. 구할 때 제곱근 이하의 약수만 구하였으며 구한 약수를 기반으로 현재의 수를 구성할 수 있는 약수의 곱을 answer에 추가합니다.
    그 후, answer을 순회하며 어떤 약수의 곱이 주어진 노란색 카펫 수와 성립할 수 있는지 비교 후 반환합니다.
'''

import math

def solution(brown, yellow):
    answer = []
    for divisor in range(3, int(math.sqrt(brown+yellow)+1)):
        if (brown+yellow) % divisor == 0:
            answer.append([(brown+yellow)/divisor, divisor])
    for i in answer:
        if (i[0] - 2) * (i[1] - 2) == yellow:
            return i