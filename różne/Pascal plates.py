def pretty_plates(plates, p):
    n = len(plates)
    k = len(plates[0])

    # g(t, i) - suma i górnych talerzy stosu t

    g = [[0 for _ in range(k + 1)] for _ in range(n)]
    for i in range(n):
        g[i][1] = plates[i][0]

    for i in range(n):
        for t in range(2, k + 1):
            g[i][t] = g[i][t - 1] + plates[i][t - 1]

    # f(w, d) - maksymalne piekno uzywające stosow od 0 do w i biorące d talerzy

    func = [[0 for _ in range(p + 1)] for _ in range(n)]

    for c in range(min(p, k) + 1):
        func[0][c] = g[0][c]

    for w in range(1, n):
        for d in range(p + 1):
            for q in range(min(d, k) + 1):
                func[w][d] = max(func[w][d], func[w - 1][d - q] + g[w][q])

    return func[n - 1][p]


if __name__ == '__main__':
    pq = [[1, 1, 3, 5, 6, 7],
          [4, 6, 4, 5, 6, 6],
          [4, 6, 5, 5, 1, 1]]
    print(pretty_plates(pq, 9))

