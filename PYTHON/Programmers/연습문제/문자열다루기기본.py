'''
https://programmers.co.kr/learn/courses/30/lessons/12918

풀이 : 문자열이 숫자로 이루어져 있는지, 문자열 길이가 4, 6 과 같은지 비교한 후 모두 True일 때 True를, 아닐 경우 False를 반환합니다.
'''

def solution(s):
    return s.isnumeric() and len(s) in (4, 6)

s = "a234"
print(solution(s))