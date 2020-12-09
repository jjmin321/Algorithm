'''
https://programmers.co.kr/learn/courses/30/lessons/12917

풀이 : 문자열을 내림차순으로 정렬하기 위해서 sorted 함수를 사용하여 리스트로 바꾼 후, ''.join()을 사용하여 리스트를 문자열로 바꾸어 반환하였습니다.
'''

def solution(s):
    return ''.join(sorted(s, reverse=True))

s = "Zbcdefg"
print(solution(s))