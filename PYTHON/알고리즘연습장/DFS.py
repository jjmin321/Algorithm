def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

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
dfs(graph, 1, visited)