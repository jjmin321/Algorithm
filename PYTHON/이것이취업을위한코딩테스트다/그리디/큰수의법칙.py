'''
배열의 크기 N, 숫자가 더해지는 횟수 M, 연속해서 K번 초과해서 더해질 수 없는 횟수인 K가 주어질 때 만들 수 있는 가장 큰 수를 구하시오.
'''

def solution(N, M, K, num):
    num.sort(reverse=True) # 4 3 2
    answer = 0
    while M > 0:
        for i in range(K):
            if M != 0:
                answer += num[0]
                M -= 1
        if M != 0:
            answer += num[1]
            M -= 1 
    return answer 
    
N, M, K = map(int, input().split())
num = list(map(int, input().split()))
print(solution(N, M, K, num))