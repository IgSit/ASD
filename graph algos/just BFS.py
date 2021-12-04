from collections import deque


def bfs(graph, start):  # neighbourhood lists implementation
    n = len(graph)
    visited = [False] * n
    queue = deque([])

    visited[start] = True
    queue.append(start)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
