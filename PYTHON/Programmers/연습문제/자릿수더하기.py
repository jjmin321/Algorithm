'''
https://programmers.co.kr/learn/courses/30/lessons/12931

풀이 : 숫자를 문자열로 바꿔 자릿수 하나씩 리스트에 넣은 후 합계를 반환하였습니다

'''

def solution(n):
    return sum([int(i) for i in str(n)])

n = 123
print(solution(n))
