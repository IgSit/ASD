# f(i) - max zysk z wycięcia drzew od indeksu o do i włącznie
# f(i) = max(f(i - 1), f(i - 2) + c_i)
# f(0) = c_0
# f(1) = max(c_0, c_1)


def black_forest(profits):
    n = len(profits)
    func = [0] * n
    func[0] = profits[0]
    func[1] = max(profits[0], profits[1])
    for i in range(2, n):
        func[i] = max(func[i - 1], func[i - 2] + profits[i])
    return func[n - 1]


if __name__ == '__main__':
    test = [1, 3, 4, 3, 4, 6, 7, 9, 10]
    print(black_forest(test))
