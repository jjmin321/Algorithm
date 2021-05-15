'''
https://programmers.co.kr/learn/courses/30/lessons/42627

풀이 : 실행해야 할 작업을 먼저 정렬한 후 모든 작업이 없어질 때까지 순회합니다. 즉시 실행할 수 있는 작업을 모두 possible_jobs 힙에 넣습니다. 만약 즉시 실행할 수 있는 작업이 없다면 가장 빠르게 실행할 
    수 있는 시간을 현재 시간으로 설정 후 다시 순회합니다. 실행 가능한 작업이 있을 경우 가장 빨리 끝낼 수 있는 작업 순으로 재정렬합니다. 그리고 작업을 수행하고, 시간을 구합니다.
'''

import heapq

def min_jobs_done_time(jobs, amount):
    now_time, total_time = 0, 0
    while jobs:
        idx = 0
        possible_jobs = []
        while idx < len(jobs) and jobs[idx][0] <= now_time:
            heapq.heappush(possible_jobs, jobs[idx])
            idx += 1
        if jobs and not possible_jobs:
            now_time = jobs[0][0]
        else:
            possible_jobs = sorted(possible_jobs, key=lambda x:x[1])
            job = heapq.heappop(possible_jobs)
            jobs.remove(job)
            total_time += now_time + job[1] - job[0]
            now_time += job[1]
    return total_time//amount

def solution(jobs):
    jobs.sort()
    answer = min_jobs_done_time(jobs, len(jobs))
    return answer