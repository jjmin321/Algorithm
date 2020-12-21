'''
https://programmers.co.kr/learn/courses/30/lessons/12930

풀이 : 공백을 기준으로 문자열을 잘라 각 문자열을 순회하며 짝수 인덱스는 대문자, 홀수 인덱스는 소문자로 바꾸었습니다. 문자 순회가 끝날 때마다 공백을 추가해주었습니다.
마지막 문자가 끝나고 공백이 추가되는 것을 [:-1]까지 반환하면서 처리했습니다.
'''

def solution(s):
    words = s.split(' ')
    answer = []
    for word in words:
        for i in range(len(word)):
            answer.append(word[i].upper()) if i % 2 == 0 else answer.append(word[i].lower())
        answer.append(' ')
    return ''.join(answer)[:-1]
s = "try hello world"
print(solution(s))