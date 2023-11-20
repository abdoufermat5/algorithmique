# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    n_min = 0
    last = 0
    i = 0
    stops.append(d)
    
    while i < len(stops):
        if stops[i] - last <= m:
            i += 1
            continue
        elif stops[i] - stops[i - 1] > m or i == 0:
            return -1
        else:
            last = stops[i - 1]
            n_min += 1
            
    return n_min


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
