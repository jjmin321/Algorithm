'''
https://programmers.co.kr/learn/courses/30/lessons/68644

풀이 : numbers의 모든 값들을 더하기 위해 이중 반복문을 사용하였으며, Python의 set 자료형을 사용해 모든 테스트 케이스를 통과하지 못해 list형으로 append, sort를 사용하여 풀었습니다
'''

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            value = numbers[i]+numbers[j]
            if not value in answer:
                answer.append(value)
    answer.sort()
    return answer

numbers = [2, 1, 3, 4, 1]
print(solution(numbers))