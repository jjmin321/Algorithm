'''
https://programmers.co.kr/learn/courses/30/lessons/42583

풀이 : 큐를 사용하여 트럭과 다리 객체를 다루었습니다 trucks_move라는 메서드를 만들어 대기 트럭의 모든 트럭이 다리에 오를 때까지 반복문을 수행하며 시간에 1을 추가하였습니다 
    그 후, 다리에 남아 있는 트럭을 1칸 옮길 때마다 시간에 1을 추가하였습니다
'''

from collections import deque

def trucks_move(time, trucks, bridge, weight):
    time += 1
    bridge.popleft()
    now_truck = trucks.popleft()
    if sum(bridge) + now_truck > weight:
        bridge.append(0)
        trucks.appendleft(now_truck)
    else:
        bridge.append(now_truck)
    return time, trucks, bridge, now_truck

def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bridge = deque([0 for i in range(bridge_length)])
    while trucks:
        time, trucks, bridge, now_truck = trucks_move(time, trucks, bridge, weight)
    while bridge:
        time += 1
        bridge.popleft()
    return time