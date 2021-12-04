# wierzchołek grafu to przedział, a krawędzie to możliwe sklejenia
from collections import deque


def prep_graph(intervals, k):
    n = len(intervals)
    if k == 1:
        return max(intervals[i][1] - intervals[i][0] for i in range(n))
    intervals.sort()
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if intervals[i][1] == intervals[j][0] or intervals[i][0] == intervals[j][1]:
                graph[i].append(j)
                graph[j].append(i)

    return longest_merged(graph, 0, intervals, k)


def longest_merged(gr, start, its, k):
    n = len(gr)
    queue = deque([])
    visited = [False] * n
    visited[start] = True
    its[start].append(1)
    queue.append(start)

    while queue:
        u = queue.popleft()
        for v in gr[u]:
            if not visited[v]:
                visited[v] = True
                its[v].append(its[u][2] + 1)
                queue.append(v)

    return max(its[j][1] - its[i][0] for i in range(n) for j in range(i + 1, n) if its[j][2] - its[i][2] + 1 <= k)


if __name__ == '__main__':
    test = [[3, 5], [2, 3], [0, 2], [-2, 0]]
    print(prep_graph(test, 2))
