from collections import deque


def get_neighbours(graph, i, j, depth):
    n = len(graph)
    m = len(graph[0])
    neighbours = []
    if i - 1 >= 0 and graph[i - 1][j] > depth:
        neighbours.append((i - 1, j))
    if j - 1 >= 0 and graph[i][j - 1] > depth:
        neighbours.append((i, j - 1))
    if i + 1 < n and graph[i + 1][j] > depth:
        neighbours.append((i + 1, j))
    if j + 1 < m and graph[i][j + 1] > depth:
        neighbours.append((i, j + 1))
    return neighbours


def bfs(graph, depth, i=0, j=0):
    n = len(graph)
    m = len(graph[0])
    queue = deque([])

    graph[i][j] = depth - 1  # visited
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        neighbours = get_neighbours(graph, x, y, depth)
        for a, b in neighbours:
            if a == n - 1 and b == m - 1:
                return True
            graph[a][b] = depth - 1  # visited
            queue.append((a, b))
    return False


if __name__ == '__main__':
    test = [[5, 5, 5, 5, 5, 5],
            [7, 1, 1, 1, 5, 7],
            [6, 5, 5, 1, 5, 1],
            [1, 1, 6, 5, 1, 8]]
    print(bfs(test, 4))
