'''
https://programmers.co.kr/learn/courses/30/lessons/42628

풀이 : 주어진 명령어를 차례대로 순회하며 삭제 명령어가 올 경우 현재 answer이 비어있는지 확인 후 최댓값과 최솟값을 삭제합니다. 만약 삽입 명령어가 온다면 heap을 통해 값을 추가합니다.
    반환할 때 배열이 비어있다면 [0, 0]을 , 그게 아니라면 최댓값과 최솟값을 차례대로 반환합니다.
'''

import heapq

def solution(operations):
    answer = []
    for operation in operations:
        if operation == "D 1":
            if answer:
                answer.remove(max(answer))
        elif operation == "D -1":
            if answer:
                heapq.heappop(answer)
        else:
            heapq.heappush(answer, int(operation[2:]))
    if not answer:
        return [0, 0]
    return max(answer), min(answer)