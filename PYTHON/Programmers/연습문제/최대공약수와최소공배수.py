'''
https://programmers.co.kr/learn/courses/30/lessons/12940

풀이 : 유클리드 호제법을 사용하여 풀었습니다. 

'''

def solution(n, m):
    num = [max(n, m), min(n, m)]
    while True:
       if num[0] % num[1] != 0: num[0], num[1] = num[1], num[0] % num[1]
       else: return [num[1], int(n * m / num[1])]

n, m = 3, 12 
print(solution(n, m))
