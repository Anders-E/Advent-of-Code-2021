from sys import stdin
from functools import reduce
from itertools import pairwise

def star1(measurements):
    return reduce(
        lambda s, pair: s + (pair[0] < pair[1]),
        pairwise(measurements),
        0
    )

def star2(measurements):
    triplets = zip(measurements, measurements[1:], measurements[2:])
    return reduce(
        lambda s, pair: s + (pair[0] < pair[1]),
        pairwise(map(sum, triplets)),
        0
    )

if __name__ == '__main__':
    measurements = [int(line) for line in stdin.readlines()]
    print(star1(measurements), end='\n\n')
    print(star2(measurements))
