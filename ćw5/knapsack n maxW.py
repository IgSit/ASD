def knapsack(weights, profits, max_w):
    #  f(i, w) - max profit of things from indexes 0 to i, having
    #            summary weight equal to w

    n = len(weights)
    func = [[0 for _ in range(max_w + 1)] for _ in range(n)]
    q = 0
    while not weights[q] <= max_w:
        q += 1
    func[q][weights[q]] = profits[q]

    for i in range(1, n):
        for w in range(1, max_w + 1):
            func[i][w] = func[i - 1][w]
            if w >= weights[i]:
                func[i][w] = max(func[i][w], func[i - 1][w - weights[i]] + profits[i])

    return func[n - 1][max_w], func


def get_solution(func, weights, profits, i, w):
    if i == 0:
        if w >= weights[0]:
            return [0]
        return []

    if w >= weights[i] and func[i][w] == func[i - 1][w - weights[i]] + profits[i]:
        return get_solution(func, weights, profits, i - 1, w - weights[i]) + [i]
    return get_solution(func, weights, profits, i - 1, w)


if __name__ == '__main__':
    weight = [4, 5, 12, 9, 1, 13]
    profit = [1, 2, 4, 5, 3, 4]
    max_weight = 30
    res, f_arr = knapsack(weight, profit, max_weight)
    print(get_solution(f_arr, weight, profit, len(weight) - 1, max_weight))
    print(res)
