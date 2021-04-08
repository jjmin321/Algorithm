'''
https://programmers.co.kr/learn/courses/30/lessons/42587

풀이 : 인쇄할 문서의 우선순위와 각 문서의 순서를 튜플로 묶은 후 queue를 사용하여 문제를 풀었습니다
   
'''

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(i, priorities[i]) for i in range(len(priorities))])
    while queue:
        document = queue.popleft()
        if max(priorities) == document[1]:
            answer += 1 
            if location == document[0]: break 
            priorities.remove(document[1])
        else:
            queue.append(document)

    return answer