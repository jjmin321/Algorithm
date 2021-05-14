'''
https://programmers.co.kr/learn/courses/30/lessons/42586

풀이 : progresses와 speeds를 zip을 사용하여 순회하여 작업 속도를 계산해 work 큐에 넣어둔 후 반복문을 통해 왼쪽에서 값을 빼내면서 그 다음 값과 비교하여 답을 구했습니다.
'''

import math
from collections import deque 

def check_before_work(done_work, work):
    count = 1
    while work and work[0] <= done_work:
        count += 1
        work.popleft()
    return count

def solution(progresses, speeds):
    answer = []
    work = deque()
    for progress, speed in zip(progresses, speeds):
        work.append(math.ceil((100-progress)/speed))
    while work:
        done_work = work.popleft()
        count = check_before_work(done_work, work)
        answer.append(count)
    return list(answer)