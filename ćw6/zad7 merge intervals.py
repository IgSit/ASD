from math import inf


# variation 1 - only ask if we can make an interval [i,j] or not
# f(i, j) - bool, czy można zrobić przedział [i,j]
# f(i, j) = OR ( f(i, k) AND f(k, j) ) dla i <= k <= j
# wpisujemy dane inwerwały jako base cases
def merge_1(points, intervals, x, y):
    max_end = max(points) + 1
    func = [[False for _ in range(max_end)] for _ in range(max_end)]
    for a, b in intervals:
        func[a][b] = True
    for i in range(max_end):
        for j in range(i + 1, max_end):
            for k in range(i, j + 1):
                if func[i][j]:
                    break
                func[i][j] = func[i][j] or (func[i][k] and func[k][j])
    return func[x][y]


# variation 2 - minimal cost of making interval [i, j]
# f(i, j) = min{f(i, k) + f(k, j), i <= k <= j}
# jeśli nie istnieje, to koszt to inf
def merge_2(points, intervals, costs, x, y):
    max_end = max(points) + 1
    func = [[inf for _ in range(max_end)] for _ in range(max_end)]
    for i in range(len(intervals)):
        a, b = intervals[i]
        if a == x and b == y:
            return 0
        func[a][b] = costs[i]
    for i in range(max_end):
        for j in range(i + 1, max_end):
            for k in range(i, j + 1):
                func[i][j] = min(func[i][j], func[i][k] + func[k][j])
    return func[x][y]


# variation 3 - najdłuższy przedział używający najwyżej k przedziałów
# f(i, j) - minimalna liczba sklejeń, by uzyskać przedział [i, j]
# f(i, j) = min( f(i, k) + f(k, j) + 1), i <= k <= j
def merge_3(points, intervals, k):
    max_end = max(points) + 1
    func = [[inf for _ in range(max_end)] for _ in range(max_end)]
    for a, b in intervals:
        func[a][b] = 0
    for i in range(max_end):
        for j in range(max_end):
            for k in range(i, j + 1):
                func[i][j] = min(func[i][j], func[i][k] + func[k][j] + 1)

    return max(b - a for a in range(max_end) for b in range(max_end) if func[a][b] <= k)


if __name__ == '__main__':
    test = [[1, 4], [3, 5], [3, 4], [1, 2], [2, 3], [4, 5]]
    p = [0] * (2 * len(test))
    c = [6, 3, 1, 3, 2, 1]
    r = 0
    for q in range(len(test)):
        p[r], p[r + 1] = test[q]
        r += 2
    p = list(set(p))
    print(merge_3(p, test, 2))
