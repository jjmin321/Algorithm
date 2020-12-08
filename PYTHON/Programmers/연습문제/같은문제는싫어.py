'''
https://programmers.co.kr/learn/courses/30/lessons/12903

풀이 : 연속되는 숫자를 구별하기 위해 arr 리스트를 순회하여 리스트의 인덱스가 0일 때 또는 그 전 인덱스와 값이 다를 때의 값들을 반환하였습니다.
'''
def solution(arr):
    answer = []
    for idx, value in enumerate(arr):
        if (idx == 0) or (arr[idx - 1] != value):
            answer.append(value)
    return answer

arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))