from math import inf


def knapsack(weights, profits, max_w):
    #  f(i, p) - min weight of things from indexes 0 to i, having
    #            summary profit equal or greater than p

    p_sum = sum(profits)
    n = len(weights)
    func = [[inf for _ in range(p_sum + 1)] for _ in range(n)]

    for q in range(profits[0] + 1):
        func[0][q] = weights[0]

    for i in range(1, n):
        for p in range(p_sum + 1):
            if profits[i] >= p:
                func[i][p] = min(weights[i], func[i - 1][p])
            else:
                func[i][p] = func[i - 1][p]
            if p >= profits[i]:
                func[i][p] = min(func[i][p], func[i - 1][p - profits[i]] + weights[i])

    for k in range(p_sum, -1, -1):
        if func[n - 1][k] <= max_w:
            return k, func


def get_solution(func, weights, profits, i, p):
    if i == 0:
        if p >= profits[0]:
            return [0]
        return []

    if p >= profits[i] and (func[i][p] == func[i - 1][p - profits[i]] + weights[i] or func[i][p] == weights[i]):
        return get_solution(func, weights, profits, i - 1, p - profits[i]) + [i]
    return get_solution(func, weights, profits, i - 1, p)


if __name__ == '__main__':
    weight = [4, 5, 12, 9, 1, 13]
    profit = [10, 8, 4, 5, 3, 7]
    max_weight = 24
    res, f_arr = knapsack(weight, profit, max_weight)
    print(get_solution(f_arr, weight, profit, len(weight) - 1, res))
    print(res)
