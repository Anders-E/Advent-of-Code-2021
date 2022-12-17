from sys import stdin
from statistics import median
from functools import cache


@cache
def arithmetic_progression(n):
    return n * (n + 1) // 2


def star1(positions):
    closest_pos = int(median(positions))
    return sum(map(lambda pos: abs(pos - closest_pos), positions))


def star2(positions):
    left = min(positions)
    right = max(positions)
    fuel_needed = [0] * (right - left)
    for x in range(left, right):
        fuel_needed[x] = sum(
            map(lambda pos: arithmetic_progression(abs(pos - x)),
                positions))
    return min(fuel_needed)


if __name__ == '__main__':
    positions = list(map(int, stdin.readline().split(',')))

    print(star1(positions), end='\n\n')
    print(star2(positions))
