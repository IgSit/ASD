from math import inf


# Minimalna ilość monet ze zbioru M potrzebna do wydania kwoty w
# F[i] - minimalna ilość monet potrzebna do wydania kwoty i
def min_coins(coins, w):
    F = [0]*(w+1)
    for c_sum in range(1, w+1):
        F[c_sum] = inf
        for coin in coins:
            if c_sum - coin >= 0:
                F[c_sum] = min(F[c_sum], F[c_sum-coin]+1)
    return F[w]


if __name__ == '__main__':
    coins = [1, 5, 8]
    print(min_coins(coins, 15))