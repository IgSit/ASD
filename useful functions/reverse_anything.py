def reverse_anything(x):
    if isinstance(x, list):
        left, right = 0, len(x) - 1
        while left < right:
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1
        return x
    if isinstance(x, str):
        new_str = ""
        index = len(x) - 1
        while index != - 1:
            new_str += x[index]
            index -= 1
        return new_str
    if isinstance(x, int):
        new_num = 0
        while x != 0:
            new_num = 10 * new_num + x % 10
            x //= 10
        return new_num
    if isinstance(x, tuple):
        new_tuple = []
        index = len(x) - 1
        while index != -1:
            new_tuple += [x[index]]
            index -= 1
        return tuple(new_tuple)


if __name__ == '__main__':
    print(reverse_anything((1, 2, 3)))
