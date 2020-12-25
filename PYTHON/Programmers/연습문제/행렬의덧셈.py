'''
https://programmers.co.kr/learn/courses/30/lessons/12950

풀이 : arr1과 arr2를 zip 내장함수를 통해 같이 순회하면서 그 안의 리스트를 또 다시 zip내장함수를 통해 순회하며 값을 더하여 반환하였습니다.

'''

def solution(arr1, arr2):
    return [[a + b for a, b in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]

arr1, arr2 = [[1, 2], [2, 3]], [[3, 4], [5, 6]]
print(solution(arr1, arr2))
