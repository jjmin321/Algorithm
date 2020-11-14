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