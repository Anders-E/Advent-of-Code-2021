from itertools import repeat
from sys import stdin
from collections import defaultdict
from functools import partial
from operator import le, add

from util import sign


def draw_line(line):
    (x1, y1), (x2, y2) = line
    x = x1 - x2
    y = y1 - y2
    x_sign = sign(x)
    y_sign = sign(y)
    x_offset = min(x1, x2) if x_sign > 0 else max(x1, x2)
    y_offset = min(y1, y2) if y_sign > 0 else max(y1, y2)

    if x1 == x2:
        xRange = repeat(x1)
    else:
        xRange = map(partial(add, x_offset), range(0, x + x_sign, x_sign))
    if y1 == y2:
        yRange = repeat(y1)
    else:
        yRange = map(partial(add, y_offset), range(0, y + y_sign, y_sign))

    return zip(xRange, yRange)


def is_diagonal(line):
    (x1, y1), (x2, y2) = line
    return x1 != x2 and y1 != y2


def star1(lines):
    grid = defaultdict(int)
    for line in lines:
        if not is_diagonal(line):
            for pos in draw_line(line):
                grid[pos] += 1
    return len(list(filter(partial(le, 2), grid.values())))


def star2(lines):
    grid = defaultdict(int)
    for line in lines:
        for pos in draw_line(line):
            grid[pos] += 1
    return len(list(filter(partial(le, 2), grid.values())))


def parse_line(line):
    (x1, y1), (x2, y2) = [
        map(int, pos.split(',')) for pos in line.split(' -> ')
    ]
    return (x1, y1), (x2, y2)


if __name__ == '__main__':
    lines = [parse_line(line) for line in stdin.readlines()]

    print(star1(lines), end='\n\n')
    print(star2(lines))
