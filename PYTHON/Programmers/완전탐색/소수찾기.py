'''
https://programmers.co.kr/learn/courses/30/lessons/42839

풀이 : 파이썬 라이브러리를 사용하여 모든 순열을 만들어 all_number에 추가합니다. 그 후 set 자료형으로 중복을 제거한 후 모든 순열의 값을 순회하며 값의 제곱근까지 반복하여 
만약 나누어 떨어지는 값이 있다면 not_prime_nums에 추가합니다. 그 후 not_prime_nums와 0, 1을 제거 후 남은 숫자의 수를 반환합니다.
'''

import math
import itertools
    
def count_prime_number(num):
    num = set(num)
    not_prime_nums = [0, 1]
    for i in num:
        for j in range(2, int(math.sqrt(i))+1): 
            if i % j == 0:
                not_prime_nums.append(i)
                break
    num -= set(not_prime_nums)
    return len(num)
    
def solution(numbers):
    all_number = []
    for i in range(len(numbers), 0, -1):
        nPr = itertools.permutations(numbers, i)
        for i in nPr:
            all_number.append(int("".join(i)))        
    return count_prime_number(all_number)