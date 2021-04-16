'''
https://programmers.co.kr/learn/courses/30/lessons/1845

풀이 : 가져가도 될 폰켓몬의 수가 총 폰켓몬 / 2기 때문에 기본적(else)으로 폰켓몬 / 2를 반환합니다. 하지만 폰켓몬의 종류가 폰켓몬 / 2 보다 적다면 총 폰켓몬 종류의 수를 반환합니다
'''

def solution(nums):
    return len(set(nums)) if len(set(nums)) <= len(nums) / 2 else len(nums) / 2