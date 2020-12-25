'''
https://programmers.co.kr/learn/courses/30/lessons/12954

풀이 : x부터 x*n까지 돌기 위해서, for range를 사용하였습니다. 양수와 음수에 따라 x*n+1 , x*n-1을 하기 위해 a를 사용하였습니다. 만약 x가 0일 경우 n만큼 0을 리스트에 추가하여 반환하였습니다.

'''

def solution(x, n):
    a = 1 if x > 0 else -1
    return [i for i in range(x, x*n+a, x)] if x != 0 else [0 for i in range(n)]

x, n = 0, 5
print(solution(x, n))
