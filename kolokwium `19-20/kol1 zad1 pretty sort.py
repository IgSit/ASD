class PrettyNum:
    def __init__(self, value, single, non_single):
        self.value = value
        self.single = single
        self.non_single = non_single


def how_pretty(num):
    digits = [0 for _ in range(10)]
    while num != 0:
        digits[num % 10] += 1
        num //= 10
    singles = non_singles = 0
    for digit in digits:
        if digit == 1:
            singles += 1
        elif digit > 1:
            non_singles += 1
    return singles, non_singles


def display_arr(arr):
    for elem in arr:
        print(elem.key, end=" ")
    print()


def pretty_sort(arr):
    n = len(arr)
    for i in range(n):
        single, non_single = how_pretty(arr[i])
        arr[i] = PrettyNum(arr[i], single, non_single)

    for i in range(2):
        counting_sort(arr, i)
        display_arr(arr)
    return arr


def counting_sort(arr, i):
    n = len(arr)
    c_arr = [0 for _ in range(10)]
    output = [0 for _ in range(n)]

    for k in range(n):
        index = arr[k].non_single if i == 0 else arr[k].single
        c_arr[index] += 1

    for k in range(1, 10):
        c_arr[k] += c_arr[k - 1]

    for k in range(n - 1, -1, -1):
        index = arr[k].non_single if i == 0 else arr[k].single
        output[c_arr[index] - 1] = arr[k]
        c_arr[index] -= 1

    for k in range(n):
        arr[n - 1 - k] = output[k]


if __name__ == '__main__':
    test = [3322, 1266, 114577, 123, 455, 2344, 67333, 1234455, 12344, 12, 134, 12, 13, 432, 543, 5434, 22]
    pretty_sort(test)
