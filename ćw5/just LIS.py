def lis(arr):
    n = len(arr)
    func = [1] * n  # f(i) - length of LIS ending at index i
    par = [-1] * n  # p(i) - parent of elem at index i (previous elem in LIS)
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and func[j] + 1 > func[i]:
                func[i] = func[j] + 1
                par[i] = j

    res_i = -1
    max_len = 1
    for k in range(n):
        if func[k] > max_len:
            max_len = func[k]
            res_i = k

    return arr, res_i, par


def print_lis(arr, res_i, par):
    if par[res_i] >= 0:
        print_lis(arr, par[res_i], par)
    print(arr[res_i], end=" ")


if __name__ == '__main__':
    test = [1, 3, 6, 3, 5, 7, 8, 3, 2, 5]
    array, idx, parents = lis(test)
    print_lis(array, idx, parents)
