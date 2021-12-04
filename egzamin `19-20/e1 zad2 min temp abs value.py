# sum(i, j) - suma elementów of i do j włącznie
# f(i, j) - minimalna największa tymczasowa suma elementow od i do j włącznie
# f(i, j) = max( abs(sum(i,j)), min(f(i + 1,j), f(i, j - 1)) ) - jeśli końcowa suma ma największa, to
# musimy ją dać jako największą tymczasowa wartosc, a tak to bierzemy minimum z największych tymczasowych
# sum o 1 krótszych

# f(i, i + 1) = sum(i, i + 1)
# f(i, i) = sum(i, i)


def opt_sum(arr):
    n = len(arr)

    p_sum = [[0 for _ in range(n)] for _ in range(n)]
    p_sum[0][0] = arr[0]
    for q in range(1, n):
        p_sum[q][0] = p_sum[q - 1][0] + arr[q]
        p_sum[0][q] = p_sum[q][0]
        p_sum[q][q] = arr[q]
    for i in range(1, n):
        for j in range(i + 1, n):
            p_sum[i][j] = p_sum[i - 1][j] - arr[i - 1]
            p_sum[j][i] = p_sum[i][j]

    func = [[-1 for _ in range(n)] for _ in range(n)]

    def rec(w, k):
        if func[w][k] >= 0:
            return func[w][k]
        if w == k:
            func[w][w] = abs(p_sum[w][w])
            return func[w][w]
        if k == w + 1:
            func[w][w + 1] = abs(p_sum[w][w + 1])
            return func[w][w + 1]

        a = rec(w + 1, k)
        b = rec(w, k - 1)
        all_sum = abs(p_sum[w][k])
        func[w][k] = max(abs(all_sum), min(a, b))
        return func[w][k]

    x = rec(0, n - 1)
    return x
