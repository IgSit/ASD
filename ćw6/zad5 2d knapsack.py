# f(i, w, h) - max val rzeczy od indeksów 0 do i włącznie, mających łączną wagę w i łączną wysokość h
# f(i, w, h) = max( f(i - 1, w, h), f(i - 1, w - w[i], h - h[i]) + p[i])
# f(0, w[0], h[0]) = p[0]

# w implementacji F[i][w][h]


def knapsack_2d(profits, weights, heights, max_w, max_h):
    n = len(profits)
    func = [[[0 for _ in range(max_h + 1)] for _ in range(max_w + 1)] for _ in range(n)]
    q = 0
    while not (weights[q] <= max_w and heights[q] <= max_h):
        q += 1
    func[q][weights[q]][heights[q]] = profits[q]

    for i in range(1, n):
        for w in range(max_w + 1):
            for h in range(max_h + 1):
                func[i][w][h] = func[i - 1][w][h]
                if w - weights[i] >= 0 and h - heights[i] >= 0:
                    func[i][w][h] = max(func[i][w][h], func[i - 1][w - weights[i]][h - heights[i]] + profits[i])

    return func[n - 1][max_w][max_h], func


def get_solution(func, weights, heights, profits, i, w, h):
    if i == 0:
        if w >= weights[0] and h >= heights[0]:
            return [0]
        return []

    if w >= weights[i] and h >= heights[i] and func[i][w][h] == func[i - 1][w - weights[i]][h - heights[i]] + profits[i]:
        return get_solution(func, weights, heights, profits, i - 1, w - weights[i], h - heights[i]) + [i]
    return get_solution(func, weights, heights, profits, i - 1, w, h)


if __name__ == '__main__':
    pr = [1, 3, 5, 3, 5]
    we = [4, 2, 2, 1, 5]
    he = [1, 3, 2, 1, 2]
    w_max, h_max = 10, 8
    res, f = knapsack_2d(pr, we, he, w_max, h_max)
    print(res)
    print(get_solution(f, we, he, pr, len(pr) - 1, w_max, h_max))
