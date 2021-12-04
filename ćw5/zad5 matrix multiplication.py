from math import inf


def matrix_multiplication(arr):
    n = len(arr) - 1  # macierzy o 1 mniej niż informacji w tablicy
    # f(i,j) = min( f(i,k) + f(i+1,k) + p_i*p_k*p_j) dla i <= k <= j
    # minimalny koszt pomnożenia ciągu macierzy od i do k + koszt pomnożenia macierzy od k+1 do j
    # i pomnożenie tych podciągów

    func = [[inf for _ in range(n)] for _ in range(n)]

    for q in range(n):
        func[q][q] = 0  # koszt mnożenia macierzy samej ze sobą

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                func[i][j] = min(func[i][j], func[i][k] + func[k + 1][j] + arr[i]*arr[k + 1]*arr[j + 1])

    return func[0][n - 1]


if __name__ == '__main__':
    test = [30, 35, 15, 5, 10, 20, 25]
    print(matrix_multiplication(test))
