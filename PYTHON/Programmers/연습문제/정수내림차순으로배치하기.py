'''
https://programmers.co.kr/learn/courses/30/lessons/12933

풀이 : 파이썬의 특징을 이용해 정수를 문자열로 바꾼 후 순회하여 리스트에 넣고 다시 문자열로 바꾼 후 다시 정수로 바꾼 후 반환하였습니다

'''

def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse = True)))

n = 118372
print(solution(n))
