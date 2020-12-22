'''
https://programmers.co.kr/learn/courses/30/lessons/12932

풀이 : 자연수를 순회하기 위해 문자열로 바꾼 후 순회하여 리스트에 한 자리 자연수로 값을 채운 뒤 0부터 끝까지 뒤에서부터 하나씩 반환하였습니다

'''

def solution(n):
    return [int(i) for i in str(n)][::-1]

n = 12345
print(solution(n))
