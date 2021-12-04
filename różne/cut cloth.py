def cut_cloth(pieces, profits, x, y):  # O(kXY)
    # pieces [(a1, b1), (a2, b2)...]
    # prices [c1, c2...]
    # f(a, b) - najlepszy zysk z pocięcia kawałka axb

    # zamieniam każdy kawałek, że jeśli jest prostokątem, to leży na dłuższym boku
    m = len(pieces)
    for q in range(m):
        s, d = pieces[q]
        if s > d:
            pieces[q] = (d, s)

    func = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
    for a in range(1, x + 1):
        for b in range(1, y + 1):
            for p in range(m):
                w, k = pieces[p]
                if a >= w and b >= k:
                    func[a][b] = max(func[a][b], profits[p] + func[w][b - k] + func[a - w][b])
                    if b <= x and a <= y:
                        func[b][a] = max(func[a][b], func[b][a])

    return func[x][y]


def another_cut(matrix, x, y):
    func = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
    for a in range(1, x + 1):
        for b in range(1, y + 1):
            try:
                func[a][b] = matrix[a][b]
            except IndexError:
                continue

            # check horizontal lines
            for h in range(1, a // 2 + 1):
                func[a][b] = max(func[a][b], func[a - h][b] + func[h][b])

            # check vertical lines
            for w in range(1, b // 2 + 1):
                func[a][b] = max(func[a][b], func[a][b - w] + func[a][w])

    return func[x][y]


if __name__ == '__main__':
    t = [(1, 3), (2, 2), (4, 3), (2, 4), (5, 1)]
    c = [1, 2, 5, 3, 2]
    print(cut_cloth(t, c, 5, 6))
    m = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 2],
         [0, 0, 2, 0, 3, 0],
         [0, 1, 0, 0, 5, 0],
         [0, 0, 3, 5, 0, 0],
         [0, 2, 0, 0, 0, 0]]
    print(another_cut(m, 5, 6))
