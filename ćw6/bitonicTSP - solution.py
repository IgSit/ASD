from math import sqrt, inf
from operator import itemgetter


def calc_dist(cities):
    n = len(cities)
    dist = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = cities[i][1], cities[i][2]
            x2, y2 = cities[j][1], cities[j][2]
            dist[i][j] = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            dist[j][i] = dist[i][j]
    return dist


def bitonic_TSP(cites):
    n = len(cites)
    cites.sort(key=itemgetter(1))
    dist = calc_dist(cites)
    func = [[inf for _ in range(n)] for _ in range(n)]
    func[0][1] = dist[0][1]

    for w in range(n):
        for k in range(n):
            func[w][k] = tsp_rec(w, k, func, dist)

    res = inf
    for i in range(n - 1):
        res = min(res, func[i][n - 1] + dist[i][n - 1])
    return res


def tsp_rec(i, j, func, dist):
    if func[i][j] != inf:
        return func[i][j]

    if i < j - 1:
        func[i][j] = tsp_rec(i, j - 1, func, dist) + dist[j - 1][j]
    else:  # i = j - 1
        best = inf
        for k in range(j - 1):
            best = min(best, tsp_rec(k, j - 1, func, dist) + dist[k][j])
        func[i][j] = best

    return func[i][j]


if __name__ == '__main__':
    C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
    print(bitonic_TSP(C))
