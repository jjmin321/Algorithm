'''
500원, 100원, 50원, 10원의 동전이 있고 거슬러 줘야 할 돈 N원이 있을 때 거슬러줄 수 있는 동전의 최소 개수를 구하라.
'''

def solution(n):
    cnt = 0
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        cnt += n // coin 
        n = n % coin
    return cnt 

n = int(input('거스름돈 N원을 입력해주세요: '))
print(solution(n))