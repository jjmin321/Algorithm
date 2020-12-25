'''
https://programmers.co.kr/learn/courses/30/lessons/17681

풀이 : bin 내장함수를 통하여 2진수로 변환, OR 비트 연산자를 활용하여 문제를 풀었습니다.
'''

def solution(n, arr1, arr2):
    arr = []
    for i, j in zip(arr1, arr2):
        binary = bin(i|j)[2:]
        binary = binary.rjust(n, '0')
        binary = binary.replace('0', ' ')
        binary = binary.replace('1', '#')
        arr.append(binary)
    return arr

n, arr1, arr2 = 5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))