'''
https://programmers.co.kr/learn/courses/30/lessons/17681

풀이 : bin 내장함수를 통하여 2진수로 변환, OR 비트 연산자를 활용하여 문제를 풀었습니다. 하지만 지도를 구성하는 일차원 배열 중 첫 번째 부분이 0인 경우, 0이 삭제되므로 rjust 내장함수를 사용해서 n자리 만큼, 부족한 자릿수를 0으로 채워주게끔 만들었습니다.
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

n, arr1, arr2 = 5, [9, 1, 28, 18, 11], [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))