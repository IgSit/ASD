# szerokość reprezentacji - długość najkrótszego substringa w danej reprezentacji
# f(i) - max szerokość reprezentacji słowa od indeksu 0 do i exclusive


from math import inf


def max_representation(word, strings):
    n = len(word)
    func = [-inf for _ in range(n + 1)]
    for i in range(n + 1):
        for string in strings:
            last_substring = word[i - len(string): i]
            if i > len(last_substring):
                if last_substring == string:
                    func[i] = max(func[i], min(func[i - len(string)], len(string)))
            elif i == len(last_substring):
                if last_substring == string:
                    func[i] = max(func[i], len(last_substring))
    return func[n]


if __name__ == '__main__':
    w = "ababbab"
    s = ["ab", "abab", "bab", "ba", "b"]
    print(max_representation(w, s))
