'''
https://programmers.co.kr/learn/courses/30/lessons/42747
구현 코드만 간단하지만 생각보다 많이 돌아왔던 문제라 복습이 필요

풀이 : 최댓값을 구하는 문제이므로 내림차순으로 정렬 후 논문 수만큼 반복문을 순회하며 i+1로 h번보다 많이 인용된 논문의 수에 현재 논문을 추가하여 h편 이상 여부를 검사하였습니다. 만약 h편 이상이라면 현재 h를 반환합니다.
'''

def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i+1 >= citations[i]:
            return i
    return len(citations)