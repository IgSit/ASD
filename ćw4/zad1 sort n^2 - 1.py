# każdą liczbę z zakresu 0, n^2 - 1 można przedstawić jako x = k * n + r,
# 0 <= k <= n - 1, 0 <= r <= n - 1
# gdzie k = x // n, r = x % n
# najpierw sortujemy po r, potem po k

def radix_sort(arr):
    for i in range(2):
        counting_sort(arr, i)
    return arr


def counting_sort(arr, i):
    n = len(arr)
    c_arr = [0 for _ in range(n)]
    output = [0 for _ in range(n)]

    for k in range(n):
        index = arr[k] % n if i == 0 else arr[k] // n
        c_arr[index] += 1

    for k in range(1, n):
        c_arr[k] += c_arr[k - 1]

    for k in range(n - 1, -1, -1):
        index = arr[k] % n if i == 0 else arr[k] // n
        output[c_arr[index] - 1] = arr[k]
        c_arr[index] -= 1

    for k in range(n):
        arr[k] = output[k]


if __name__ == '__main__':
    test = [1, 24, 3, 0, 16, 35, 48]
    print(radix_sort(test))
