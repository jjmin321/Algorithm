'''
https://programmers.co.kr/learn/courses/30/lessons/12903

풀이 : 주어진 문자열이 짝수일 경우, 중앙에 위치한 2글자를 반환, 홀수일 경우 중앙에 위치한 1글자를 반환하였습니다
'''
def solution(s):
    if len(s) % 2 == 0:
        return s[int(len(s)/2-1):int(len(s)/2+1)]
    else:
        return s[int(len(s)/2)]

s = 'abcde'
print(solution(s))