'''
https://programmers.co.kr/learn/courses/30/lessons/42584

풀이 : 주식 가격이 담긴 배열을 순회하며 더 낮은 가격이 나올때까지 다음 인덱스부터 이중 포문을 통해 순회합니다.  
    더 낮은 가격이 나온다면 배열에 더 낮은 가격 인덱스 - 현재 인덱스 를 배열에 추가하고 반복문을 빠져나옵니다. 만약 더 낮은 가격이 나오지 않는다면 배열의 길이 -1 - 현재 인덱스를 배열에 추가합니다
'''

def solution(prices):
    answer = []
    for idx, price in enumerate(prices): 
        for next_idx in range(idx+1, len(prices)):
            if prices[next_idx] < price:
                answer.append(next_idx - idx)
                break
        else:
            answer.append(len(prices)-1-idx)
    return answer