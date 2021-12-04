# f(i, j) - minimalna liczba skoków, by znaleźć się na i, mając co najmniej j jednostek energii

from math import inf


def zbigniew(arr):
    n = len(arr)
    _sum = sum(arr)
    F = [[inf for _ in range(_sum + 1)] for _ in range(n)]

    for i in range(arr[0] + 1):
        F[0][i] = 0

    for i in range(1, n):
        for y in range(_sum):
            for k in range(i):
                eng = y + i - k - arr[i]
                if eng < i - k or eng > _sum or eng < 0:
                    continue
                F[i][y] = min(F[i][y], F[k][eng] + 1)

    return min(F[n - 1][i] for i in range(_sum + 1))


if __name__ == '__main__':
    test = [1, 2, 2, 2, 2, 2, 2]
    print(zbigniew(test))
