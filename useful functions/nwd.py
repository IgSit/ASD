def nwd(a, b):
    minimum = min(a, b)
    for i in range(minimum, 0, -1):
        if a % i == b % i == 0:
            return i


if __name__ == '__main__':
    print(nwd(3, 0))
