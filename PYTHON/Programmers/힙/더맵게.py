'''
https://programmers.co.kr/learn/courses/30/lessons/42626

풀이 : 힙을 사용하여 문제를 풀었습니다. 먼저 배열을 정렬한 뒤 계산할 수 있을 때까지 반복문을 순회합니다. 만약 배열에서 가장 작은 값이 K보다 낮다면 계속 새로운 음식을 만듭니다.
      만약 모든 값이 K보다 높아지거나 더 이상 새로운 음식을 만들 수 없다면 반복문을 종료한 후 모든 음식이 K 이상인지 검사 후 새로운 음식을 만든 횟수를 리턴합니다.
'''

import heapq

def mix(scoville):
    a = heapq.heappop(scoville)
    b = heapq.heappop(scoville)
    heapq.heappush(scoville, a+b*2)
    
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while len(scoville)-1:
        if scoville[0] < K:
            answer += 1
            mix(scoville) 
        else: 
            break
    if scoville[0] < K:
        return -1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))