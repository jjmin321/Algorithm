'''
어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 수행하려 한다. 이 때 두 과정을 수행해야 하는 최소 횟수를 구하시오.
1. N에서 1을 뺀다 
2. N을 K로 나눈다 
'''

'''
오답 1: 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다는 것을 확인하지 않았다.
'''
# N, K = map(int, input().split())
# cnt = 0
# while N != 1:
#     if N // K >= 1:
#         N //= K
#     else:
#         N -= 1
#     cnt += 1
# print(cnt)

N, K = map(int, input().split())
cnt = 0
while N != 1:
    if N // K >= 1 and N % K == 0:
        N //= K
    else:
        N -= 1
    cnt += 1
print(cnt)