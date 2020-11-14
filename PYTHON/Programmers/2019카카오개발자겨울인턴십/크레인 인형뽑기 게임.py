'''
https://programmers.co.kr/learn/courses/30/lessons/64061

풀이 : moves 배열을 하나씩 순회하며 2차원 배열로 인형들이 들어있는 board에서 인형을 뽑아 data에 넣습니다.
      data, 즉 인형 바구니에 인형이 1개 초과로 들어간다면 원래 있던 인형과 새로 들어간 인형을 비교하여 같은 인형일 경우 바구니에서 제거 후 answer에 2를 더했습니다.
'''

def solution(board, moves) :
    data = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0 :
                data.append(board[j][i-1])
                if len(data) > 1:
                    if data[len(data)-2] == data[len(data)-1]:
                        data.pop(len(data)-2), data.pop(len(data)-1)
                        answer += 2
                board[j][i-1] = 0
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))