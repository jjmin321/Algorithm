'''
https://programmers.co.kr/learn/courses/30/lessons/12943

풀이 : 계산 횟수가 500회 이상 넘어가면 -1을 반환합니다. 500회 이하까지는 짝수와 홀수에 맞게 처리하게끔 하였습니다.

'''

def solution(num):
    cnt = 0
    while num != 1:
        if cnt == 500: return -1
        if num % 2 == 0: num = num/2
        else: num = num * 3 + 1
        cnt += 1
    return cnt

num = 626331
print(solution(num))
