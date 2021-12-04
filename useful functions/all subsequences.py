def generate_subsequences(array):
    n = len(array)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(array[i:j])
    return result


if __name__ == '__main__':
    test = [1, 2, 3, 4]
    print(generate_subsequences(test))
