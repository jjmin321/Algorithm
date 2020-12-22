'''
https://programmers.co.kr/learn/courses/30/lessons/12935

풀이 : 내림차순으로 정렬한 뒤 맨 마지막 인덱스의 값을 리스트에서 제거한 후 반환하였습니다. 만약 빈 배열이라면 [-1]을 반환하게끔 하였습니다.

'''

def solution(arr):
    arr.remove(sorted(arr, reverse = True)[-1])
    return [-1] if arr == [] else arr

arr = [4, 3, 2, 1]
print(solution(arr))
