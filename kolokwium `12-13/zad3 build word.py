def build_word(w1, w2, w3):
    array = [0 for _ in range(26)]
    for letter in w1:
        array[ord(letter) - 97] += 1
    for letter in w2:
        array[ord(letter) - 97] += 1
    for letter in w3:
        array[ord(letter) - 97] -= 1
        if array[ord(letter) - 97] < 0:
            return False
    return True


if __name__ == '__main__':
    print(build_word("ada", "oko", "odakoo"))
