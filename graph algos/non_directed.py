from collections import deque


# variation I - one BFS with removing edges - o(n^2)


def bfs_directed1(graph, start):  # neighbourhood lists implementation
    n = len(graph)
    visited = [False] * n
    queue = deque([])

    visited[start] = True
    for child in graph[start]:
        visited[child] = True
        queue.append([child, start])

    while queue:  # O(n)
        u, anc = queue.popleft()
        go_back = False
        for v in graph[u]:
            if v == anc:
                go_back = True
            if not visited[v]:
                visited[v] = True
                queue.append([v, u])
        if not go_back:
            return False


def non_directed(graph):
    n = len(graph)
    for i in range(n):
        if len(graph[i]) > 1:
            if not bfs_directed1(graph, i):
                return False
    return True


# variation II - linear BFS for every point - o(n^2)


def bfs_directed(graph, start):  # neighbourhood lists implementation
    queue = deque([])
    visited = [False] * len(graph)

    for child in graph[start]:  # O(n)
        queue.append([child, start])
    graph[start] = []
    visited[start] = True

    while queue:  # O(n)
        u, anc = queue.popleft()
        go_back = False
        for v in graph[u]:
            if v == anc:
                go_back = True
            if not visited[v] and [v, u] not in queue:  # O(n)
                queue.append([v, u])
        visited[u] = True
        if not go_back:
            return False
        graph[u].remove(anc)  # O(n)

    return True


# variation III - for every point we check its neighbours - o(|E|)


def is_not_directed(graph):
    n = len(graph)
    for i in range(n):

        queue = deque()
        for child in graph[i]:
            queue.append((child, i))

        while queue:
            u, anc = queue.popleft()
            go_back = False
            for v in graph[u]:
                if v == anc:
                    go_back = True

            if not go_back:
                return False

    return True


if __name__ == '__main__':
    test = [[1, 2],
            [0, 2],
            [0, 1, 3],
            [2]]
    print(is_not_directed(test))
