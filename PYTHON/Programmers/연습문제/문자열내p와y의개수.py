'''
https://programmers.co.kr/learn/courses/30/lessons/12916

풀이 : 문자열 메서드인 count를 통해 p와 y의 개수를 비교한 후 같다면 True, 다르다면 False를 반환하였습니다.
'''

def solution(s):
    return True if s.count('p') + s.count('P') == s.count('y') + s.count('Y') else False

s = "pPoooyY"
print(solution(s))