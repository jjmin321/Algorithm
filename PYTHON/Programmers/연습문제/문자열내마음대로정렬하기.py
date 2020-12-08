'''
https://programmers.co.kr/learn/courses/30/lessons/12915

풀이 : 만약 n번째 자리 알파벳이 같을 경우 사전순으로 정렬하여야 하므로 정렬을 먼저 한 후, 정렬함수 내에 사용할 수 있는 람다를 이용해 n번째 자리 알파벳으로 정렬을 하였습니다. 
'''

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])

strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))
