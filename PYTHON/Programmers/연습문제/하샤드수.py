'''
https://programmers.co.kr/learn/courses/30/lessons/12947

풀이 : 정수를 문자열로 바꾼 후 순회하여 다시 정수로 바꾸어 1자리씩 순회하였습니다. x를 x의 모든 자릿수 총 합으로 나누어 나누어 떨어지면 True를, 아니라면 False를 반환하였습니다.

'''

def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0 

x = 10
print(solution(x))
