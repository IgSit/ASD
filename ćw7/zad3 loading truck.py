# bierz najcięższy możliwy
# Działa, bo każda cięższa waga może zostać zbudowana za pomocą mniejszych wag
# D - d
# Niech istnieje algorytm optymalny, który przynajmniej raz nie bierze najcięższego możliwego
# 1) z mniejszych wag nie można zbudować wagi cięższej (nie ma tylu powtórzeń danych mniejszych wag)
#    wtedy optymalny algorytm zapełni ciężarówkę w mniejszych stopniu, stąd sprzeczność
# 2) z mniejszych wag można zbudować wagę cieższą
#    wtedy istnieje taki moment, że biorąc wagi mniejsze, w pewnym momencie będą się one sumowały
#    do tej cięższej wagi, czyli można te wszystkie lżejsze zamienić na jeden cięższy
#    stąd sprzeczność, algorytm optymalny nie użyje najmniejszej możliwej ilości pakunków

from math import log2


def loading(weights, volume):
    n = int(log2(max(weights)) + 1)
    packages = [0] * n
    for weight in weights:
        packages[int(log2(weight))] += 1

    res = []

    i = n - 1
    while i != -1:
        while volume >= 2 ** i and packages[i] > 0:
            res.append(2 ** i)
            volume -= 2 ** i
            packages[i] -= 1
        i -= 1
    return res


if __name__ == '__main__':
    w = [1, 2, 2, 2, 4, 8, 8, 16]
    print(loading(w, 27))
