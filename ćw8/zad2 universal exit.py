from collections import deque


# todo: źle zinterpretowałem uniwersalne ujście i poniżej jest kod sprawdzający, czy z każdego
# todo: wierzchołka jest scieżka do ujścia, a nie krawędź


def is_exit(graph, v):
    return True if sum(graph[v]) == 0 else False


def has_uni_exit(graph):
    n = len(graph)
    candidates = [i for i in range(n) if is_exit(graph, i)]
    if len(candidates) > 1:
        return False

    for candidate in candidates:
        visited = [False] * n
        queue = deque([])

        visited[candidate] = True
        queue.append(candidate)

        while queue:
            u = queue.popleft()
            for i in range(n):
                if graph[i][u] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

        if sum(visited) == len(visited):  # every point has a path to candidate
            return True
    return False


if __name__ == '__main__':
    test = [[0, 1, 0, 0, 1],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0]]
    print(has_uni_exit(test))
