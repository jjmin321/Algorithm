from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end= ' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

graph = [
    [],
    [2, 4],
    [5, 7],
    [9, 10],
    [6],
    [2, 8],
    [4, 10, 11],
    [2, 8, 9],
    [5, 7],
    [3, 7],
    [3, 6],
    [6]
]

visited = [False] * 12
BFS(graph, 1, visited)