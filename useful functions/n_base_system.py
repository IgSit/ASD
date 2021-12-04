def number_to_n_system(num, n):
    cnt = 1
    while num >= n ** cnt:
        cnt += 1
    result = [None for _ in range(cnt)]
    index = cnt - 1
    while num != 0:
        rest = num % n
        result[index] = rest if rest < 10 else chr(ord("A") + rest - 10)
        num //= n
        index -= 1
    return result


if __name__ == '__main__':
    number = 13
    k = 2
    print(number_to_n_system(number, k))
