from queue import PriorityQueue
from math import inf
from operator import itemgetter


# dostajemy graf w postaci listy sąsiedztwa - (wierzch, waga) w kolejnych listach

def decreasing_edges(graph, s, t):
    n = len(graph)
    queue = PriorityQueue()
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s] = 0
    queue.put([0, inf, s])  # dodajemy [dist, waga_ostatniej, wierzch]

    for i in range(n):
        graph[i].sort(reverse=True, key=itemgetter(1))

    while not queue.empty():
        distance, last, v = queue.get()

        for i in range(len(graph[v]) - 1, -1, -1):
            u, weight = graph[v][i]
            if last > weight:
                queue.put([distance + weight, weight, u])
                if distance + weight < dist[u]:
                    dist[u] = distance + weight
                    parent[u] = v
                graph[v].pop()

    return get_path(parent, s, t), dist[t]


def get_path(parent, s, t):
    res = []
    while parent[t] != -1:
        res.append(t)
        t = parent[t]
    res.append(s)
    res.reverse()
    return res


if __name__ == '__main__':
    graph1 = [[(1, 9)],
              [(0, 9), (6, 8), (2, 10)],
              [(1, 10), (3, 4)],
              [(2, 4), (4, 5)],
              [(3, 5), (5, 6)],
              [(4, 6), (6, 7)],
              [(5, 7), (2, 8)]]

    graph2 = [[(1, 10), (3, 4)],
              [(2, 10)],
              [],
              [(2, 3)]]

    graph3 = [[(1, 10), (2, 5)],
              [(0, 10), (2, 1), (3, 3), (4, 2)],
              [(0, 5), (1, 1), (4, 4), (3, 6)],
              [(2, 6), (1, 3), (4, 3), (5, 2)],
              [(3, 3), (2, 4), (1, 2), (5, 1)],
              [(4, 1), (3, 2)]]

    print(decreasing_edges(graph3, 0, 3))
