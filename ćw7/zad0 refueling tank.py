from math import inf


def bin_search(arr, val, left, right):
    if val >= arr[right]:
        return right
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] > val:
            right = mid
        elif arr[mid] < val:
            left = mid
        else:
            return mid
    return (left + right) // 2

# variation 1 - minimalna liczba tankowań, żeby dojechać do celu
# Algorytm - tankuj do pełna i jedź do najdalszej możliwej stacji
# Załóżmy, że optymalny algorytm przynajmniej raz nie jedzie do najdalszej możliwej stacji i
# ma mniejszą liczbę postojów
# Wtedy przy tej samej ilości postojów na stacjach co "nasz" algorytm, optymalny pokona mniejszą
# trasę. Zatem, aby dojechać do celu, ten optymalny algorytm musi stanąć minimum tyle samo razy co
# nasz algorytm, stąd sprzeczność


def tank_1(stations, fuel, t):
    n = len(stations)
    i = fuel
    counter = 0
    prev_station = None
    if i < t and i < stations[0]:  # nie dojadę ani do celu, ani do pierwszej stacji
        return inf
    while i < t:
        furthest_station = bin_search(stations, i, 0, n - 1)
        if prev_station == furthest_station:  # nie dojadę nawet do najbliższej stacji
            return inf
        prev_station = furthest_station
        counter += 1
        i = stations[furthest_station] + fuel
    return counter


# variation 2 - na stacji są różne ceny paliwa i możemy tankować, tyle, ile chcemy
# na początku dojedź do najtańszej stacji
# potem dwie opcje
# 1) jeśli w maks. zasięgu jest tańsza stacja, to zatankuj tylko tyle, ile trzeba, by do niej dojechać
# (do pierwszej tańszej)
# 2) jeśli w zasięgu nie ma tańszej, to tankuj do pełna i jedź do następnej stacji sprawdzić war. 1)
# Dowód poprawności:
# Załóżmy, że optymalny algorytm co najmniej raz nie tankuje do pełna na najtańszej stacji w zasięgu
# lub co najmniej raz tankuje więcej na droższe stacji, niż trzeba, by dojechać do tańszej
# 1) jeśli nie tankuje do pełna na najtańszej w zasiegu, to w przyszłości będzie musiał kupić więcej droższego paliwa,
# jeśli nie dojedzie do celu (koszt optymalnego większy lub równy od naszego)
# 2) jeśli kupi więcej paliwa na droższej stacji niż trzeba, by dojechać do najtańszej, to po prostu
# zapłaci więcej, niż może (koszt większy od naszego)
# Stąd sprzeczność, algorytm optymalny nie jest optymalny


def tank_2(stations, prices, fuel, t):
    n = len(stations)
    pos = 0
    pos_idx = 0
    fuel_tank = fuel
    cost = 0
    if stations[0] > fuel:
        return inf

    while pos < t:
        if pos_idx < n - 1:
            if stations[pos_idx + 1] - stations[pos_idx] > fuel:
                return inf
        furthest_station = bin_search(stations, pos + fuel_tank, 0, n - 1)  # index
        cheapest_station = cheapest(prices, pos_idx, furthest_station)  # index
        fuel_tank -= (stations[cheapest_station] - pos)
        pos = stations[cheapest_station]
        pos_idx = cheapest_station  # dojechałem na najtańszą możliwą

        furthest_station = bin_search(stations, pos + fuel, 0, n - 1)  # index
        cheapest_station = cheapest(prices, pos_idx, furthest_station)  # index
        if pos_idx == cheapest_station:  # jestem na najtańszej w zasięgu - tankuj do pełna i pojedź do następnej stacji
            if t - pos < fuel:
                last = t - pos
                if fuel_tank >= last:
                    return cost
                return cost + (last - fuel_tank) * prices[pos_idx]

            cost += (fuel - fuel_tank) * prices[cheapest_station]
            pos = stations[cheapest_station + 1]
            pos_idx += 1
            if pos_idx > n - 1 and t - (pos + fuel_tank) > 0:
                return inf
            fuel_tank = fuel - (stations[pos_idx] - stations[pos_idx - 1])
        else:  # jadę do pierwszej tańszej stacji, tankuję tylko tyle, żeby dojechać
            if t - pos < fuel:
                last = t - pos
                if fuel_tank >= last:
                    return cost
                return cost + (last - fuel_tank) * prices[pos_idx]

            p = pos_idx + 1
            while prices[p] >= prices[pos_idx]:
                p += 1
            dist = stations[p] - stations[pos_idx]
            cost += (dist - fuel_tank) * prices[pos_idx]
            pos = stations[p]
            pos_idx = p
            fuel_tank = 0


def cheapest(prices, start, end):  # start, end - indexes
    idx = start
    min_price = prices[start]
    for i in range(start, end + 1):
        if prices[i] < min_price:
            min_price = prices[i]
            idx = i
    return idx


# variation 3 - minimalny koszt dotarcia do t, ale jak tankujemy, to do pełna
# f(i) - minimalny koszt dotarcia do stacji o idx i i do pełna na niej
# f(i) = min{ f(i-k) + c_i*dist(i,k), dist(i, k) <= max_fuel} k - indeks wcześniejszej stacji


def tank_3(stations, prices, fuel, t):
    n = len(stations)

    if stations[0] > fuel:
        return inf
    stations.append(t)
    for q in range(n):
        if stations[q + 1] - stations[q] > fuel:
            return inf

    func = [inf] * n
    func[0] = stations[0] * prices[0]
    for i in range(1, n):
        if stations[i] <= fuel:
            func[i] = stations[i] * prices[i]
        k = i - 1
        while 0 <= k >= i - fuel:
            func[i] = min(func[i], func[k] + prices[i] * (stations[i] - stations[k]))
            k -= 1

    return func[n - 1]


if __name__ == '__main__':
    test = [2, 6, 9, 14]
    c = [2, 3, 3, 4]
    print(tank_3(test, c, 6, 15))
