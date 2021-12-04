def prime(x):
    if x == 2 or x == 3 or x == 5:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
        if x % i == 0:
            return False
    return True


def factorize(num):
    if prime(num):
        return [num]
    result = []
    i = 2
    while num != 1:
        if num % i == 0:
            result.append(i)
            while num % i == 0:
                num //= i

        i += 1
    return result


if __name__ == '__main__':
    print(factorize(45))
