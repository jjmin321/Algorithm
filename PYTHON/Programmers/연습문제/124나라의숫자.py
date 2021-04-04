'''
https://programmers.co.kr/learn/courses/30/lessons/12899

풀이 : 재귀함수를 사용하여 풀었습니다. 만약 n이 3이하면 각각 1, 2, 4를 반환하는데 이를 이용하며 재귀를 실행하였습니다
'''

def division(n):
    return (n-1) // 3 

def back_number(n):
    if n % 3 == 1:
        return '1'
    elif n % 3 == 2:
        return '2'
    else:
        return '4'

def translate_number(n):
    if n <= 3:
        return back_number(n)
    return translate_number(division(n)) + back_number(n)

def solution(n):
    return translate_number(n)

print(solution(5))