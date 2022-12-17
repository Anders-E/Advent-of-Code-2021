from sys import stdin
from collections import namedtuple
import re


Target = namedtuple('Target', ['min_x', 'max_x', 'min_y', 'max_y'])


def within_target(target, x, y):
    return (
        target.min_x <= x <= target.max_x and target.min_y <= y <= target.max_y
    )


def beyond_target(target, x, y):
    return x > target.max_x or y < target.min_y


def trajectory_height(target, xv, yv, x_origin=0):
    x = x_origin
    y = 0
    height = y
    while not beyond_target(target, x, y):
        height = max(height, y)
        if within_target(target, x, y):
            return height
        x += xv
        y += yv
        xv = max(0, xv - 1)
        yv -= 1
    return -1


def star1(target):
    max_height = 0
    for yv in range(160):
        height = trajectory_height(target, 0, yv, target.min_x)
        max_height = max(max_height, height)
    return max_height


def star2(target):
    hits = 0
    for yv in range(-154, 160):
        for xv in range(0, target.max_x + 1):
            hit = trajectory_height(target, xv, yv) != -1
            hits += hit
    return hits


if __name__ == '__main__':
    target = Target(*map(int, re.match(
        r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)',
        stdin.readline()
    ).groups()))  # type: ignore

    print(star1(target), end='\n\n')
    print(star2(target))
