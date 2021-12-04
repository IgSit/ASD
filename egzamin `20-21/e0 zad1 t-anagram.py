# Dla każdej litery sprawdzamy okno o środku będącym indeksem tej litery i promieniu t
# Zaczynamy sprawdzanie od lewej, bo jeśli teraz nie wykorzystamy czegoś, co potencjalnie zostało,
# to przy następnym wywołaniu będzie jeszcze dalej
# Obliczeniowa O(nt)
# Pamięciowa O(n)
from collections import deque


def t_anagrams(word1, word2, t):
    n = len(word1)
    used = [False for _ in range(n)]
    for i in range(n):
        found = False
        for k in range(max(0, i - t), min(n - 1, i + t) + 1):
            if word1[i] == word2[k] and not used[k]:
                used[k] = True
                found = True
                break
        if not found:
            return False
    return True


# Rozwiązanie liniowe
# Tworzymy tablice na każdą litere i dodajemy pod odpowiednie miejsca wystapienia tych liter
# w pierwszym słowie
# Potem, iterujac po drugim słowie, sciagamy z odpowiednich miejsc najwczesniejsze wystapienie
# (jesli bysmy nie brali najwczesniejszego, to przy kolejnym wywolaniu tej litery byloby jeszcze dalej)
# i sprawdzamy warunek, czy roznica indeksow jest niewieksza od t
# Obliczeniowa O(n)
# Pamieciowa O(n)


def better_t_anagrams(word1, word2, t):
    n = len(word1)
    positions = [deque() for _ in range(26)]
    for i in range(n):
        positions[ord(word1[i]) - 97].append(i)
    for i in range(n):
        try:
            first = positions[ord(word2[i]) - 97].popleft()
        except IndexError:
            return False
        if abs(i - first) > t:
            return False
    return True
