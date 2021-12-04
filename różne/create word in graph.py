from math import inf


def make_graph(edges, n):
    res = [[] for _ in range(n)]
    for u, v, weight in edges:
        res[u].append([v, weight])
        res[v].append([u, weight])
    return res


def cheapest_word(edges, letters, word):
    w = len(word)
    n = len(letters)
    dist = [inf for _ in range(n)]
    graph = make_graph(edges, n)
    for q in range(n):
        if letters[q] == word[0]:
            dist[q] = 0
    for i in range(w - 1):
        s, t = word[i], word[i + 1]

        for u in range(n):
            if letters[u] == s:
                for v, weight in graph[u]:
                    if letters[v] == t:
                        if dist[u] + weight < dist[v]:
                            dist[v] = dist[u] + weight

        for k in range(n):
            dist[k] = inf if letters[k] != t else dist[k]

    return min(dist)


if __name__ == '__main__':
    L = ["k", "k", "o", "o", "t", "t"]
    E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
    print(cheapest_word(E, L, "kto"))
