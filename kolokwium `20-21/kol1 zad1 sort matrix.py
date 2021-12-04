from random import randint


def quick_select(arr, k, left, right):  # k to indeks liczby
    while True:
        p = randPartition(arr, left, right)
        if p == k:
            return
        elif p < k:  # bierzemy prawą część
            left = p + 1
        else:  # bierzemy prawą część
            right = p - 1


def randPartition(arr, left, right):
    n = len(arr)
    d = randint(left, right)
    arr[right // n][right % n], arr[d // n][d % n] = arr[d // n][d % n], arr[right // n][right % n]
    return partition(arr, left, right)


def partition(arr, left, right):
    n = len(arr)
    x = arr[right // n][right % n]
    i = left
    for j in range(left, right):
        if arr[j // n][j % n] >= x:
            arr[i // n][i % n], arr[j // n][j % n] = arr[j // n][j % n], arr[i // n][i % n]
            i += 1

    arr[i // n][i % n], arr[right // n][right % n] = arr[right // n][right % n], arr[i // n][i % n]
    return i


def median(arr):
    n = len(arr)
    small = (n * n) // 2 - n // 2
    big = small + n - 1
    quick_select(arr, small, 0, n * n - 1)
    quick_select(arr, big, small + 1, n * n - 1)

    row = n // 2
    if n % 2 == 1:
        for i in range(n):
            arr[i][i], arr[row][i] = arr[row][i], arr[i][i]
    else:
        for i in range(n // 2):
            arr[i][i], arr[row][i] = arr[row][i], arr[i][i]
        for i in range(n // 2, n):
            arr[i][i], arr[row - 1][i] = arr[row - 1][i], arr[i][i]

    for w in range(1, row + 1):
        for k in range(w + 1):
            arr[w][k], arr[n - 1 - w][n - 1 - k] = arr[n - 1 - w][n - 1 - k], arr[w][k]
