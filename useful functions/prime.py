def prime(x):
    if x == 2 or x == 3 or x == 5:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
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
