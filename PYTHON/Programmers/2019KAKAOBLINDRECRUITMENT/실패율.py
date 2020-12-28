'''
https://programmers.co.kr/learn/courses/30/lessons/42889

풀이 : 오름차순으로 각 스테이지별 현재 성공하지 못한 사람의 수를 계산하여 count 리스트에 넣었습니다. count 리스트를 통해 각 스테이지별 실패율을 구했으며 , 실패율이 높은 스테이지 순으로 
answer 리스트에 추가해 반환하였습니다. 만약 실패율이 같다면 오름차순으로 반환합니다.
'''

def solution(N, stages):
    count = [stages.count(i) for i in range(1 ,N+2)]
    failure_rate, answer = [], []
    for i in range(N):
        if sum(count[i:]) != 0: failure_rate.append(count[i] / sum(count[i:]))
        else: failure_rate.append(0)
    for i in range(N):
        for j in range(N):
            if max(failure_rate) == failure_rate[j]: 
                answer.append(j+1)
                failure_rate[j] = -1
                break
        if sum(failure_rate) == -1*N: 
            break
    return answer

N, stages = 10, [1, 2, 1, 2]
print(solution(N, stages))