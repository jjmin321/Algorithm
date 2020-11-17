'''
https://programmers.co.kr/learn/courses/30/lessons/12901

풀이 : day에 월마다의 총 일수를 넣었고, 1월 1일이 금요일이니 day_name에 금요일부터 목요일까지 순서대로 넣어두었습니다. 
그 후 이때까지 지나간 총 달의 일수와 현재 일수를 더하여 총 일수를 구해 day_name의 7로 나눈 나머지 - 1 값의 인덱스를 반환하였습니다
'''

def solution(a, b):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_name = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    for i in range(a-1):
        b += day[i]
    return day_name[b%7-1]

a = 5
b = 24
print(solution(a, b))
