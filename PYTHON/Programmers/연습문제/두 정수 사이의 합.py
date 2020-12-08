'''
https://programmers.co.kr/learn/courses/30/lessons/12912

풀이 : 더 작은 정수를 a, 더 큰 정수를 b에 넣은 뒤 a부터 b까지 순회하여 모두 합친 값을 반환함.
'''

def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a, b+1))
a, b = 3, 5
print(solution(a, b))