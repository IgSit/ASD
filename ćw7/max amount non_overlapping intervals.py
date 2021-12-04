# Algorytm - bierz ten, który kończy się najwcześniej

# Rozważmy moment, gdy nasz algorytm uniemożliwia wybór optymalny
# Wybrany przez nas przedział kończy się wcześniej lub tak samo jak
# przedział z algorytmu opt. - obydwa te przedziały muszą na siebie nachodzić
# (inaczej sprzeczność, optymalna ścieżka nie byłaby optymalna). Możemy zamienić
# przedział wybrany z algorytmu opt. z naszym przedziałem. Stąd sprzeczność,
# nasz algorytm nie uniemożliwia skonstruowania rozwiązania optymalnego

from operator import itemgetter


def max_non_overlapping(intervals):
    n = len(intervals)
    intervals.sort(key=itemgetter(1))
    res = [intervals[0]]
    end = intervals[0][1]
    i = 1
    while i <= n - 1:
        while intervals[i][0] < end and i <= n - 1:
            i += 1
        if i <= n - 1:
            res.append(intervals[i])
            end = intervals[i][1]
            i += 1
    return res


if __name__ == '__main__':
    test = [[1, 3], [2, 3], [0, 3], [0, 4], [3, 4], [0, 1]]
    print(max_non_overlapping(test))
