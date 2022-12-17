from sys import stdin
from itertools import pairwise
from collections import Counter


def polymerize(template, rules, iterations):
    pairs = [''.join(pair) for pair in pairwise(template)]
    pair_counts = Counter(pairs)
    char_counts = Counter(template)

    for _ in range(iterations):
        new_pair_counts = Counter()
        for pair, pair_count in pair_counts.items():
            new_char = rules[pair]
            char_counts[new_char] += pair_count
            new_pair_a = pair[0] + new_char
            new_pair_b = new_char + pair[1]
            new_pair_counts[new_pair_a] += pair_count
            new_pair_counts[new_pair_b] += pair_count
        pair_counts = new_pair_counts

    return char_counts


def star1(template, rules):
    counts = polymerize(template, rules, 10).values()
    return max(counts) - min(counts)


def star2(template, rules):
    counts = polymerize(template, rules, 40).values()
    return max(counts) - min(counts)


if __name__ == '__main__':
    template = stdin.readline().rstrip()
    stdin.readline()
    rules = {
        a: b for
        a, b in [line.rstrip().split(' -> ') for line in stdin.readlines()]
    }

    print(star1(template, rules), end='\n\n')
    print(star2(template, rules))
