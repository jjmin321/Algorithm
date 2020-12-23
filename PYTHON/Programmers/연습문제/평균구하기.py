'''
https://programmers.co.kr/learn/courses/30/lessons/12944

풀이 : 리스트 내 모든 값을 합친 후 개수만큼 나눠 반환하였습니다.

'''

def solution(arr):
    return sum(arr) / len(arr)

arr = [1, 2, 3, 4]
print(solution(arr))
