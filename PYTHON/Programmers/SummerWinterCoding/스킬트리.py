'''
https://programmers.co.kr/learn/courses/30/lessons/49993

풀이 : for in ~ else 를 사용하여 불필요한 변수를 생성하지 않으며 비교하여 풀었습니다
'''

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = list(skill)
        for s in skill_tree:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer