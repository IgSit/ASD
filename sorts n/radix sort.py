from random import randint


def radix_sort(arr):
    maximum = max(arr)
    div = 1
    while maximum // div != 0:
        counting_sort(arr, div)
        div *= 10
    return arr


def counting_sort(arr, div):
    n = len(arr)
    c_arr = [0] * 10
    output = [0] * n

    for i in range(n):
        index = (arr[i] // div) % 10
        c_arr[index] += 1

    for i in range(1, 10):
        c_arr[i] += c_arr[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // div) % 10
        output[c_arr[index] - 1] = arr[i]
        c_arr[index] -= 1

    for i in range(n):
        arr[i] = output[i]


def test_sort():
    rr = (0, 1000)
    n = 10000
    m = 10
    for i in range(m):
        arr = [randint(rr[0], rr[1]) for _ in range(n)]
        good_sort = sorted(arr)
        test = radix_sort(arr)
        if test != good_sort:
            print("Incorrect")
            print(test)
            exit()
    print("Correct")


if __name__ == '__main__':
    test = [1, 43, 32, 665, 43, 24, 6, 3, 22]
    print(radix_sort(test))
