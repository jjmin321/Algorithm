'''
https://programmers.co.kr/learn/courses/30/lessons/12910

풀이 : 연속되는 숫자를 구별하기 위해 arr 리스트를 순회하여 리스트의 인덱스가 0일 때 또는 그 전 인덱스와 값이 다를 때의 값들을 반환하였습니다.
'''

def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]

arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))