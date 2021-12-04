def chessboard(arr):
    n = len(arr)
    func = [[0] * n for _ in range(n)]
    func[0][0] = arr[0][0]
    for i in range(1, n):
        func[0][i] = func[0][i - 1] + arr[0][i]
        func[i][0] = func[i - 1][0] + arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            func[i][j] = min(func[i][j - 1], func[i - 1][j]) + arr[i][j]

    x = get_path(func, arr)
    return func[n - 1][n - 1], x


def get_path(f, a):
    n = len(a)
    res = [a[n - 1][n - 1]]
    i = j = n - 1
    while not (i == j == 0):
        if j - 1 >= 0:
            if f[i][j] == f[i][j - 1] + a[i][j]:
                res.append(a[i][j - 1])
                j -= 1
                continue
        if i - 1 >= 0:
            if f[i][j] == f[i - 1][j] + a[i][j]:
                res.append(a[i - 1][j])
                i -= 1

    left, right = 0, len(res) - 1
    while left < right:
        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1
    return res


if __name__ == '__main__':
    test = [[7, 2, 4],
            [3, 4, 6],
            [5, 5, 4]]
    print(chessboard(test))