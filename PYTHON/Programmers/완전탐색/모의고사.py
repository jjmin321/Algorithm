'''
https://programmers.co.kr/learn/courses/30/lessons/42840

풀이 : 답과 수포자들이 찍는 방식을 비교하여 score 배열에 각 수포자들의 점수를 넣은 후 각 수포자들의 점수를 반복문으로 돌아 최대값의 점수에 해당하는 모든 사람을 반환하였습니다 
'''

def solution(answers):
    result = []
    scores = [0, 0, 0]
    person_first = [1, 2, 3, 4, 5]
    person_second = [2, 1, 2, 3, 2, 4, 2, 5]
    person_third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, answer in enumerate(answers):
        if answer == person_first[i%len(person_first)]:
            scores[0] += 1
        if answer == person_second[i%len(person_second)]:
            scores[1] += 1
        if answer == person_third[i%len(person_third)]:
            scores[2] += 1
    for person, score in enumerate(scores):
        if score == max(scores):
            result.append(person+1) 
    return result

answers = [1,3,2,4,2]
print(solution(answers))