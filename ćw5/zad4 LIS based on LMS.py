# F[i][j] - lms from 0 to i-th pos in first arr and from 0 to j-th in second arr
def lms(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    func = [[0 for _ in range(m + 1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr1[i - 1] == arr2[j - 1]:
                func[i][j] = func[i-1][j-1] + 1
            else:
                func[i][j] = max(func[i-1][j], func[i][j-1])
    return func[n][m]


def lis(arr):
    s = sorted(arr)
    return lms(arr, s)


if __name__ == '__main__':
    a = [1, 4, 5, 6, 7, 1]
    print(lis(a))
