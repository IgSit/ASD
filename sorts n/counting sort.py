def counting_sort(arr, k):
    n = len(arr)
    c_arr = [0] * k
    output = [0] * n
    for i in range(n):  # count occurrences of each value
        c_arr[arr[i]] += 1
    for i in range(1, k):  # count how many elements is greater or equal to each element (index == value)
        c_arr[i] += c_arr[i - 1]
    for i in range(n - 1, -1, -1):
        c_arr[arr[i]] -= 1
        output[c_arr[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = output[i]


if __name__ == '__main__':
    test = [5, 2, 7, 3, 8, 3, 2, 8, 9, 1, 3, 6, 3, 0]
    counting_sort(test, 10)
    print(test)
    print(sorted(test))
