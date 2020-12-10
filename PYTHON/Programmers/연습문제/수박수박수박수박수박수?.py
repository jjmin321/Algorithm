'''
https://programmers.co.kr/learn/courses/30/lessons/12922

풀이 : 0부터 n미만까지 반복하여 0과 짝수일 때는 수, 홀수일 때는 박을 추가한 문자열을 반환하였습니다.
'''

def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0 : answer = answer + '수'
        else : answer = answer + '박'
    return answer

n = 3
print(solution(n))