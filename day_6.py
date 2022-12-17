from sys import stdin
from collections import Counter, defaultdict


def simulate_fish(timers, days):
    for _ in range(days):
        timers = defaultdict(int, {
            time - 1: n for time, n in timers.items()
        })
        timers[6] += timers[-1]
        timers[8] = timers[-1]
        if -1 in timers:
            del timers[-1]

    return timers


def star1(timers):
    return sum(simulate_fish(timers, 80).values())


def star2(timers):
    return sum(simulate_fish(timers, 256).values())


if __name__ == '__main__':
    timers = [int(timer) for timer in stdin.readline().split(',')]

    print(star1(Counter(timers)), end='\n\n')
    print(star2(Counter(timers)))
