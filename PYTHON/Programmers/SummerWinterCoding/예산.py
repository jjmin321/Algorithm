'''
https://programmers.co.kr/learn/courses/30/lessons/12982

풀이 : d를 오름차순으로 정렬한 뒤 반복문으로 순회하며 budget에서 하나씩 값을 뺐습니다. 만약 값을 빼면 budget이 0미만이 된다면 즉시 반환합니다.
'''

def solution(d, budget):
    d.sort()
    total = 0
    for i in d:
        if budget - i >= 0:
            budget -= i
            total += 1
        else: break
    return total

d, budget = [1, 3, 2, 5, 4], 9
print(solution(d, budget))