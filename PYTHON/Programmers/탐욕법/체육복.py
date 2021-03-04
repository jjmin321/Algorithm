'''
https://programmers.co.kr/learn/courses/30/lessons/42862

풀이 : 여분 체육복을 가져온 학생이 체육복을 도난당하는 경우, 빌려줄 수 없기 때문에 먼저 반복문을 한 번 순회하며 처리를 해준 다음 체육복을 도난당한 학생과 여분 체육복을 가져온 
      학생을 반복문을 순회하며 비교해 빌려줄 수 있는 경우, 여분 체육복을 리스트에서 제거한 후, 체육복을 입은 학생의 수에 1을 추가하였습니다
'''

def solution(n, lost, reserve):
    answer = n-len(lost)
    for idx, data in enumerate(lost):
        for j in reserve:
            if data == j:
                answer += 1
                lost[idx] = -1 
                reserve.remove(j)
                break
    for i in lost:
        for j in reserve:
            if i-1 == j or i+1 == j:
                answer += 1
                reserve.remove(j)
                break
    
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))