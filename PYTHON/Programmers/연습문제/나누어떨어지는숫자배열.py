'''
https://programmers.co.kr/learn/courses/30/lessons/12910

풀이 : arr 리스트를 순회하여 divisor로 나누어떨어지는 값들만 모아 오름차순으로 정렬하여 반환합니다. 만약 값이 없다면 [-1]을 반환합니다.
'''

def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]

arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))