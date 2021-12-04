def lis(arr):
    n = len(arr)
    func = [1] * n  # f(i) - length of LIS ending at index i
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and func[j] + 1 > func[i]:
                func[i] = func[j] + 1

    return arr, max(func), func


def print_all_lis(arr, max_len, func, i, result):
    if max_len == 0:
        print(result)
        return
    for k in range(i, -1, -1):
        if func[k] == max_len:
            result[max_len - 1] = arr[k]
            print_all_lis(arr, max_len - 1, func, k, result)


if __name__ == '__main__':
    test = [2, 1, 4, 3]
    array, res, func_arr = lis(test)
    print_all_lis(array, res, func_arr, len(array) - 1, [-1] * res)
