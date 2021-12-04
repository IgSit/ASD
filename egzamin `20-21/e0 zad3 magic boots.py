from queue import PriorityQueue
from math import inf


def magic_boots(graph, s, t):
    n = len(graph)
    dist = [[inf for _ in range(2)] for _ in range(n)]
    visited = [[False for _ in range(2)] for _ in range(n)]

    queue = PriorityQueue()
    dist[s][0] = dist[s][1] = 0
    queue.put([dist[s][0], s, 0])
    queue.put([dist[s][1], s, 1])
    # 1 oznacza, że używam teraz butów
    # 0 oznacza, że nie używam butów
    # zatem z każdego wierzchołka 0 mogę iść do i do innego 0, i do 1
    # natomiast z 1 mogę iśc tylko do 0

    while not queue.empty():
        d, u, i = queue.get()
        if visited[u][i]:
            continue
        visited[u][i] = True

        if i == 0:  # idę normalnie, jedną krawędź, mogę w następnym ruchu użyć butów
            for v in range(n):
                if graph[u][v]:
                    rel_d = d + graph[u][v]
                    if not visited[v][0] and rel_d < dist[v][0]:
                        dist[v][0] = rel_d
                        queue.put([dist[v][0], v, 0])
                    if not visited[v][1] and rel_d < dist[v][1]:
                        dist[v][1] = rel_d
                        queue.put([dist[v][1], v, 1])

        else:  # używam teraz stumilowych butów, w następnym ruchu nie mogę użyć
            for v in range(n):
                if graph[u][v]:
                    jump = graph[u][v]
                    for w in range(n):
                        if graph[v][w]:
                            s_jump = max(jump, graph[v][w])
                            rel_d = d + s_jump
                            if not visited[w][0] and rel_d < dist[w][0]:
                                dist[w][0] = rel_d
                                queue.put([dist[w][0], w, 0])

    return min(dist[t][0], dist[t][1])
