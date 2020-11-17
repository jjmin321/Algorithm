'''
https://programmers.co.kr/learn/courses/30/lessons/42748

풀이 : commands를 순회하여 각각의 command들을 가져와 첫 번째 ~ 세 번째까지의 커맨드를 cmd에 저장해두었다가 반복문이 끝날 때 sorted라는 내장함수를 사용하여 답을 구했다
'''

def solution(array, commands):
    answer = []
    cmd = [0, 0, 0]
    for command in commands:
        cmd[0], cmd[1], cmd[2] = command
        answer.append(sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]] 
print(solution(array, commands))