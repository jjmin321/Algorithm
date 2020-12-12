'''
https://programmers.co.kr/learn/courses/30/lessons/70128

풀이 : zip 내장함수를 사용하여 a, b를 한 리스트에 모은 후 그 리스트를 순회하며 같은 인덱스 값들을 곱한 값을 리스트에 각각 넣은 후 모든 값을 합하여 반환하였습니다.
'''

def solution(a, b):
    return sum([x*y for x, y in zip(a, b)])

a, b = [1, 2, 3, 4], [-3, -1, 0, 2]
print(solution(a, b))