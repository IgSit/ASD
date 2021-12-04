from collections import deque


def is_duple(graph):
    n = len(graph)
    queue = deque([])
    sides = [-1] * n

    queue.append(0)
    sides[0] = 0

    while queue:
        v = queue.popleft()
        cnt = (sides[v] + 1) % 2
        for u in graph[v]:
            if sides[u] == -1:
                sides[u] = cnt
                queue.append(u)
            elif sides[u] != cnt:
                return False

    return True


if __name__ == '__main__':
    test = [[1, 2],
            [0],
            [0, 3],
            [2, 4, 6],
            [3, 5],
            [4, 6],
            [3, 5]]
    print(is_duple(test))
