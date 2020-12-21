'''
https://programmers.co.kr/learn/courses/30/lessons/12919

풀이 : 파이썬 리스트 내장함수를 통해 Kim의 인덱스 위치를 찾고 그에 맞게 반환하였습니다.
'''

def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))

seoul = ["Jane", "Kim"]
print(solution(seoul))