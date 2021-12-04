# sortujemy klocki po początkach
# bierzemy klocek najwcześniej zaczynający się
# następnie mamy zbiór klocków, które możemy położyć "za" tym pierwszym klockiem (w tym samym poziomie)
# z tego zbioru bierzemy najwcześniej zaczynający się, bo jeśli wzielibyśmy taki, który nie zaczyna
# się najwcześniej, to w następnych poziomach na pewno nie położymy tego, który zaczynał się najwcześniej -
# - będzie dziura, klocek wisi w powietrzu, sprzeczność
# ustawiamy tak naszą wieżę klocków poziomami, i albo dojdziemy do końca, albo któregoś klocka nie będzie
# się dało położyć

# w przypadku powtórzeń końców algorytm działałby o tyle, że przy każdej równości końców rozgałęziałby się i sprawdzał
# wszystkie możliwości, co jest tak nieefektywne, że można powiedzieć, że nie działa
# np. klocki [1, 2], [1, 3], [3, 4] - musiałby wziąć konczacy sie pozniej przy rownosci ( wziac [1,3] )
# np. klocki [1, 2], [1, 3], [2, 4] - musiałby wziać konczacy się wczesniej przy rownosci ( wziac [1, 2] )
from math import inf


def are_blocks(arr):
    for elem in arr:
        if elem:
            return True
    return False


def build_pyramid(blocks):
    n = len(blocks)
    for i in range(n):
        blocks[i].append(i)
    blocks.sort()
    res = []
    breaks = []
    while are_blocks(blocks):
        i = 0
        end = -inf
        while i < n:
            if blocks[i]:
                if end <= blocks[i][0]:
                    if end != blocks[i][0]:
                        breaks.append((end, blocks[i][0]))
                    a, b, _ = blocks[i]
                    for x, y in breaks:
                        if (x < a and b < y) or a < x < b or a < y < b:
                            return False
                    res.append(blocks[i][2])
                    end = blocks[i][1]
                    blocks[i] = None
            i += 1

    return res


if __name__ == '__main__':
    test = [[2, 4], [4, 5], [3, 6], [5, 7]]
    print(build_pyramid(test))
