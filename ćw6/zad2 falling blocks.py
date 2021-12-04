# szukam lis pod względem zawierania, muszę usunąć wszystkie, które nie pasują do lis,
# a jest ich n - lis_len


def how_many_to_delete(arr):
    n = len(arr)
    func = [1] * n  # f(i) - length of LIS ending at index i
    for i in range(n):
        for j in range(i):
            if arr[j][0] <= arr[i][0] and arr[j][1] >= arr[i][1] and func[j] + 1 > func[i]:
                func[i] = func[j] + 1

    lis_len = max(func)
    return n - lis_len


if __name__ == '__main__':
    test = [[0, 3], [0, 3], [2, 3], [5, 6], [3, 5]]
    print(how_many_to_delete(test))
