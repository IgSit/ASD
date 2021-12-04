# f(i, l, r) - biorąc samochody od indeksu 0 do i włącznie, mając długość l lewego pasa
# i długość r prawego pasa
# f(i, l, r) = f(i - 1, l - a[i], r) or f(i - 1, l, r - a[i])
# warunki graniczne:
# f(0, a[0], 0) = True
# f(0, 0, a[0]) = True

# kolejność w implementacji F[l][r][i]


def loading_ship(arr, length):
    n = len(arr)
    length += 1
    func = [[[False for _ in range(n)] for _ in range(length)] for _ in range(length)]

    func[arr[0]][0][0] = True
    func[0][arr[0]][0] = True

    for i in range(1, n):
        for left in range(length):
            for right in range(length):
                put_on_left = func[left - arr[i]][right][i - 1] if left - arr[i] >= 0 else False
                put_on_right = func[left][right - arr[i]][i - 1] if right - arr[i] >= 0 else False
                func[left][right][i] = put_on_left or put_on_right

    for i in range(n - 1, -1, -1):
        for left in range(length):
            for right in range(length):
                if func[left][right][i]:
                    return i + 1  # ilość samochodów o jeden większa od indeksu ostatniego auta


if __name__ == '__main__':
    test = [1, 4, 5, 4]
    print(loading_ship(test, 8))
