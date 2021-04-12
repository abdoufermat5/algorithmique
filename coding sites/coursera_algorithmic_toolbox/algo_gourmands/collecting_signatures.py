# python3

from collections import namedtuple
from itertools import combinations
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments = sorted(segments, key=lambda s: s.start, reverse=False)
    segments = [set(range(seg.start, seg.end + 1)) for seg in segments]
    res = []
    i = 0
    if len(segments) <= 1:
        return len(segments)
    while i in range(len(segments)):
        l = [segments[i]]
        j = i
        c = 0
        while j < len(segments)-1 and min(segments[j+1]) in segments[i]:
            l.append(segments[j+1])
            j += 1
            c += 1
        
        res.append(segments[i].intersection(*l[:]))
        
        if c != 0:
            i += c+1
        else:
            i += 1
    el = []
    if len(res) == 1:
        el = list(res[0])
        resultat = set(el)
        return resultat
    for s in range(len(res)-1):
        if res[s] != set():
            if res[s+1] != set() and max(res[s]) not in res[s+1]:
                el.append(max(res[s]))
            else:
                el.append(min(res[s]))
    if res[-1] != set():
        if min(res[-1]) not in res[-2] and len(res) != 1:
            el.append(max(res[-1]))
        else:
            el.append(min(res[-1]))
    resultat = set(el)
    return resultat


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
