def all_subsets(array):
    size = len(array)
    result = []

    def generate_subsets(subset=None, i=0):
        if subset is None:
            subset = []

        subset.sort()
        if len(subset) > 0 and subset not in result:
            result.append(subset)

        for j in range(i, size):
            return generate_subsets(subset + [array[j]], i + 1) or\
                generate_subsets(subset, i + 1)

    generate_subsets()
    return result


if __name__ == '__main__':
    test = [1, 2, 3, 1]
    print(all_subsets(test))
