arr = [[0 for column in range(3)] for row in range(3)]
r, c = 1, 1
# 1, 1을 기준으로 시계방향 사방탐색 
# 시계방향: 상 우 하 좌
# 네 가지 방향 탐색 
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 1

for i in range(4):
    arr[r + dr[i]][c + dc[i]] = cnt
    cnt += 1

for i in arr:
    print(i)
