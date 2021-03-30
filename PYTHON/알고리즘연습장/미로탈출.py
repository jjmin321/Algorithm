# from collections import deque 

# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i] 
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 graph[nx][ny] = graph[x][y] + 1
#     return graph[n-1][m-1]

    

# n, m = map(int, input().split())
# graph = [] # 미로의 정보가 들어갈 그래프
# for i in range(n):
#     graph.append(list(map(int, input()))) 
# dx = [-1, 1, 0, 0] # 그래프의 첫 번째 인덱스 상, 하, 좌, 우 
# dy = [0, 0, -1, 1] # 그래프의 두 번째 인덱스 상, 하, 좌, 우
# print(bfs(0, 0))

from collections import deque

def Bfs(graph, size):
    Queue = deque([(0,0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Queue:
        x, y = Queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= size[0] or ny < 0 or ny >= size[1]:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                Queue.append((nx, ny))
    return graph[size[0]-1][size[1]-1]

graph = []
n, m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input())))
print(Bfs(graph, [n, m]))