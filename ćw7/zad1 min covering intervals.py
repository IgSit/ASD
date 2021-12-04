# strategia - posortuj punkty i zaczynaj nowy przedział od perwszego niepokrytego


def covering_intervals(points):
    n = len(points)
    points.sort()
    cnt = 0
    end = points[0] - 1
    for i in range(n):
        if points[i] > end:
            cnt += 1
            end = points[i] + 1
    return cnt


if __name__ == '__main__':
    test = [0.25, 0.5, 1.6]
    print(covering_intervals(test))
