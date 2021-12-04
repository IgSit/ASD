# wierzchołek grafu to początek/koniec przedziału, krawędź - przedział
# pytamy o to, czy da się z odcinków skleić dany przedział
from collections import deque


def can_merge(graph, a, b):
    n = len(graph)
    visited = [False] * n
    visited[a] = True
    queue = deque([])
    queue.append(a)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v] and v < b:
                visited[v] = True
                queue.append(v)
            if v == b:
                return True

    return False


def prep_to_bfs(intervals, a, b):
    points = []
    for x, y in intervals:
        points.extend([x, y])

    start = min(points)
    end = max(points)
    norm_arr = [0] * (end - start + 1)
    for elem in points:
        norm_arr[elem] += 1

    i = 0
    for k in range(len(norm_arr)):
        if norm_arr[k] != 0:
            norm_arr[k] = i
            i += 1
    graph = [[] for _ in range(i)]
    for x, y in intervals:
        graph[norm_arr[x]].append(norm_arr[y])
        graph[norm_arr[y]].append(norm_arr[x])
    return can_merge(graph, norm_arr[a], norm_arr[b])


if __name__ == '__main__':
    inter = [[-1, 4], [0, 1], [-6, 3], [1, 3]]
    print(prep_to_bfs(inter, 0, 4))
