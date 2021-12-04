# proste, weź medianę, jeśli jest jedna, lub dowolny punkt z przedziału domkniętego <m1, m2>, jeśli
# mediany są dwie
# w naszej implementacji bierzemy większą medianę, jeśli są dwie (krótki kod)


def xd(points):
    return points[len(points) // 2]


if __name__ == '__main__':
    test = [1, 4, 6, 7, 8, 9]
    print(xd(test))
