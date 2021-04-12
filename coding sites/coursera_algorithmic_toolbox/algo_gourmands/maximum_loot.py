# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    p_per_w = [p / w for (p, w) in zip(prices, weights)]
    dans_le_sac = 0
    valeur_sac = 0
    while dans_le_sac != capacity and len(p_per_w) > 0:
        i_max = p_per_w.index(max(p_per_w))
        if weights[i_max] + dans_le_sac >= capacity:
            valeur_sac += (capacity - dans_le_sac) * p_per_w[i_max]
            dans_le_sac += (capacity - dans_le_sac)
            weights.pop(i_max)
        else:
            dans_le_sac += weights[i_max]
            valeur_sac += weights[i_max] * p_per_w[i_max]
            weights.pop(i_max)
        p_per_w.pop(i_max)
    
    return float(valeur_sac)
    

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
