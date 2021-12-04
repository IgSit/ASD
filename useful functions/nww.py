def nww(a, b):
    maximum = max(a, b)
    for i in range(maximum, a * b + 1):
        if i % a == i % b == 0:
            return i


if __name__ == '__main__':
    print(nww(7, 7))
