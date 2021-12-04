# wartość podziału - wartość jego najgorszego podciągu (o najmniejszej sumie elementow)
# znajdz podzial o maksymalnej wartosci <=> znajdz podzial, ktory posiada najwieksza wartosc podciagu
# o minimalnej sumie

# f(i, j) - maksymalna wartosc podzialu od 0 do i przedmiotow na j czesci
# rozwiazanie - f(n - 1, k) - mamy n - 1 elementow i k podziałow
# f(i, j) = max(min( f(i - o, j - 1), sum(a_(i - o + 1)...a(i) )))


def max_min(arr, k):
    n = len(arr)
    func = [[0 for _ in range(k + 1)] for _ in range(n)]
    all_sum = 0
    for q in range(n):
        all_sum += arr[q]
        func[q][1] = all_sum  # tyle, jaką sumę ma 1 podzial od 0 do q przedmiotow
    for i in range(1, n):
        for j in range(2, k + 1):
            for o in range(i + 1):
                first = func[i - o][j - 1]
                second = sum(arr[i - o + 1:i + 1])
                func[i][j] = max(func[i][j], min(first, second))

    return func[n - 1][k]


if __name__ == '__main__':
    test = [1, 3, 4, 7]
    x = 3
    print(max_min(test, x))
